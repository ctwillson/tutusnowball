import json
import time
import pandas as pd
import asyncio
import sys
import traceback
from aiohttp import ClientSession
import pysnowball as ball
import my_common
from my_common import mypush
# stock_list = ['SZ000001','SZ000004']
tasks = []
ball.set_token()
df = pd.read_csv('testdata/attention/zg.csv')
stock_list = df['ts_code']
price_zg = df['last_zg']
stock_notify = df['notify']
stock_down_notify = df['down_notify']
stock_up_notify = df['up_notify']

logger = my_common.MyLog(__name__,__file__)
logger.instance()
mypush.pushplus('begin','price detect begin')
async def getprice():
    sem = asyncio.Semaphore(1000)
    async with ClientSession() as session:
        for symbol in stock_list:
            # print(symbol)
            tasks.append(asyncio.create_task(ball.quotec_async(str(symbol),sem,session)))
        while(True):
            results = await asyncio.gather(*tasks)
            # print(results)
            for index,data in enumerate(results):
                data = json.loads(data)
                try:
                    tmp = data['data']['quote']['current']
                    print(stock_down_notify)
                    if(price_zg.iloc[index] <= tmp and abs(tmp - price_zg.iloc[index]) <= 0.05 and stock_notify[index]):
                        mypush.pushplus(stock_list[index],'equal 0.05!')
                        stock_notify[index] = False
                    elif (tmp < price_zg.iloc[index] and stock_down_notify.iloc[index]):
                        mypush.pushplus(stock_list[index],'sell! down 0.05!')
                        stock_down_notify.iloc[index] = False
                    elif(tmp >= price_zg.iloc[index] * 1.01 and stock_up_notify.iloc[index] and (not stock_notify.iloc[index]) and (stock_down_notify.iloc[index])):
                        mypush.pushplus(stock_list[index],'buy!up 0.05!')
                        stock_up_notify.iloc[index] = False
                except:
                    print(traceback.print_exc())
                    mypush.pushplus('error','mayde cannot get the stock data')
                    sys.exit(0)
                # logger.logerr(str(tmp) + str(price_zg.iloc[index]))
            time.sleep(1)
            # if(price_zg.iloc[index] > tmp):
            #     print(tmp)
        # 
def run():
    asyncio.run(getprice())
if __name__ == '__main__':
    run()

# while(True):
#     for ts_code in 
#     price_dic = ball.quotec('SH601066')
#     print(price_dic['data']['quote']['current'])
#     if(price_dic['data']['quote']['current'] > 35.5) :
#         my_common.pushplus('SH601066','over 35.5')
#     elif(price_dic['data']['quote']['current'] < 34.2):
#         my_common.pushplus('SH601066','below 34.2')
#     time.sleep(1)