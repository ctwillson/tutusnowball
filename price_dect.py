import json
from my_common import mylog
import time
import pandas as pd
import asyncio
import sys
import os
import traceback
from aiohttp import ClientSession
import pysnowball as ball
import my_common
from my_common import mypush
import datetime
import tushare as ts
from mootdx.quotes import Quotes
# stock_list = ['SZ000001','SZ000004']
dir_path = os.path.dirname(os.path.abspath(__file__))
PERCENT = 0.02
# tasks = []
ball.set_token()
df = pd.read_csv(dir_path+'/testdata/attention/zg.csv')
pd.set_option('display.max_columns', None)
stock_list = df.loc[:,'ts_code'].copy()
price_zg = df.loc[:,'last_zg'].copy()
stock_notify = df.loc[:,'notify'].copy()
stock_down_notify = df.loc[:,'down_notify'].copy()
stock_up_notify = df.loc[:,'up_notify'].copy()
 
buystock = pd.read_csv(dir_path+'/testdata/attention/buystock.csv')
buystock_down_notify = buystock.loc[:,'down_notify'].copy()
logger = my_common.MyLog(__name__,dir_path + '/mylogs/price_detect.log')
logger.instance()
mypush.pushplus('begin','price detect begin')

def check_tradedate():
    ts_token = os.getenv('TS_TOKEN')
    print('ts_token = ' + ts_token)

    ts.set_token(ts_token)
    pro = ts.pro_api()
    cal = str(datetime.date.today().strftime('%Y%m%d'))
    start_date = cal
    trade_date = pro.trade_cal(exchange='', start_date=start_date, end_date=cal)
    if(trade_date.iloc[-1,-1] == 0):
            print('not trading date')
            sys.exit(0)

async def getprice():
    sem = asyncio.Semaphore(1000)
    async with ClientSession() as session:
        # for symbol in stock_list:
        #     # print(symbol)
        #     if(sys.version_info < (3,7)):
        #         tasks.append(asyncio.ensure_future(ball.quotec_async(str(symbol),sem,session)))
        #     else:
        #         tasks.append(asyncio.create_task(ball.quotec_async(str(symbol),sem,session)))
        while(True):
            tasks = []
            for symbol in stock_list:
                # print(symbol)
                if(sys.version_info < (3,7)):
                    tasks.append(asyncio.ensure_future(ball.quotec_async(str(symbol),sem,session)))
                else:
                    tasks.append(asyncio.create_task(ball.quotec_async(str(symbol),sem,session)))
            results = await asyncio.gather(*tasks)
            error_count = 0
            # print(results)
            for index,data in enumerate(results):
                # if data is None:
                #     error_count = error_count + 1
                #     if(error_count == 10):
                #         mypush.pushplus('error','mayde cannot get the stock data')
                #     # print(data)
                #     time.sleep(10)
                #     continue
                try:
                    data = json.loads(data)
                    tmp = data['data']['quote']['current']
                    # print(stock_down_notify)
                    if(price_zg.iloc[index] <= tmp and abs(tmp - price_zg.iloc[index]) <= 0.05 and stock_notify[index]):
                        mypush.pushplus(stock_list[index],'equal 0.05!')
                        stock_notify.iloc[index] = False
                    elif (tmp < price_zg.iloc[index] and stock_down_notify.iloc[index]):
                        mypush.pushplus(stock_list[index],'sell! down 0.05!')
                        stock_down_notify.iloc[index] = False
                    elif(tmp >= price_zg.iloc[index] * 1.01 and stock_up_notify.iloc[index] and (not stock_notify.iloc[index]) and (stock_down_notify.iloc[index])):
                        mypush.pushplus(stock_list[index],'buy!up 0.05!')
                        stock_up_notify.iloc[index] = False
                except json.JSONDecodeError:
                    error_count = error_count + 1
                    if(error_count == 10):
                        mypush.pushplus('error','continue , mayde cannot get the stock data')
                    logger.logerr(data)
                    time.sleep(1)
                    continue
                except:
                    logger.logerr(traceback.print_exc())
                    mypush.pushplus('error','mayde cannot get the stock data')
                    sys.exit(0)
                # logger.logerr(str(tmp) + str(price_zg.iloc[index]))
            print('done sleep!')
            time.sleep(10)
            # sys.exit(0)
            # if(price_zg.iloc[index] > tmp):
            #     print(tmp)
        # 
def price_mootdx():
    check_tradedate()
    client = Quotes.factory(market='std')
    stock_mt = stock_list.apply(lambda x:x[2:]).to_list()
    last_close_list = []
    error_count = 0
    # print(stock_mt)
    while True:
        # try:
        # price_list = []
        # print(len(stock_mt))
        # start = datetime.datetime.now()
        # for i in range(0, len(stock_mt), 80):
        #     stock_mt_2 = stock_mt[i: i + 80]
        #     try:
        #         # client = Quotes.factory(market='std')
        #         df = client.quotes(symbol=stock_mt_2)
        #         price_list.extend(df.loc[:,'price'].to_list())
        #         # time.sleep(1)
        #     except:
        #         print('price_mootdx error')
        #         logger.logerr(traceback.print_exc())
        #         time.sleep(5)
        #         continue
        
        # end = datetime.datetime.now()
        # print(price_list)
        # print('Running time: %s Seconds'%(end - start))
        # # print(price_list)
        # for index,data in enumerate(price_list):
        #     try:
        #         tmp = data
        #         # print(tmp)
        #         if(price_zg.iloc[index] <= tmp and abs(tmp - price_zg.iloc[index]) <= 0.05 and stock_notify[index]):
        #             mypush.pushplus(stock_list[index],'equal 0.05! now price = ' + str(tmp))
        #             stock_notify.iloc[index] = False
        #         elif (tmp < price_zg.iloc[index] and stock_down_notify.iloc[index]):
        #             mypush.pushplus(stock_list[index],'sell! down 0.05! now price = ' + str(tmp))
        #             stock_down_notify.iloc[index] = False
        #         elif(tmp >= price_zg.iloc[index] * 1.01 and stock_up_notify.iloc[index] and (not stock_notify.iloc[index]) and (stock_down_notify.iloc[index])):
        #             mypush.pushplus(stock_list[index],'buy!up 0.05! now price = ' + str(tmp))
        #             stock_up_notify.iloc[index] = False
        #     # except json.JSONDecodeError:
        #     #     error_count = error_count + 1
        #     #     if(error_count == 10):
        #     #         mypush.pushplus('error','continue , mayde cannot get the stock data')
        #     #     logger.logerr(data)
        #     #     time.sleep(1)
        #     #     continue
        #     except:
        #         logger.logerr(traceback.print_exc())
        #         mypush.pushplus('error','mayde cannot get the stock data')
        #         sys.exit(0)
        try:
            df = client.quotes(symbol=buystock.loc[:,'ts_code'].apply(lambda x:x[2:]).to_list())
            if (len(last_close_list) == 0):
                last_close_list = df.loc[:,'last_close'].to_list()
            # print(df)
            # sys.exit(0)
            buystock_price = (df.loc[:,'price'].to_list())
            for index,data in enumerate(buystock_price):
                    tmp = data
                    # print(tmp)
                    if(tmp < buystock.loc[:,'last_zg'][index] and buystock_down_notify[index]):
                        mypush.pushplus(buystock.loc[:,'ts_code'][index],'buystock force sell!!! now price = ' + str(tmp))
                        buystock_down_notify[index] = False
                    if(tmp <= last_close_list[index]*(1-PERCENT)):
                        last_close_list[index] = tmp
                        mypush.pushplus(buystock.loc[:,'ts_code'][index],'buystock price down!!! now price = ' + str(tmp))
                    elif (tmp >= last_close_list[index]*(1+PERCENT)):
                        mypush.pushplus(buystock.loc[:,'ts_code'][index],'buystock price up!!! now price = ' + str(tmp))
                        last_close_list[index] = tmp
                    else:
                        pass
            error_count = 0
            # print(last_close_list)
            # time.sleep(10)
                    
        except:
            error_count = error_count + 1
            logger.logerr(traceback.print_exc())
            if(error_count == 10):
                mypush.pushplus('error','mayde cannot get the stock data')
            #sys.exit(0)
            time.sleep(1)
            continue
        # sys.exit(0)
def run():
    # if(sys.version_info < (3, 7)):
    #     asyncio.get_event_loop().run_until_complete(getprice())
    # else:
    #     asyncio.run(getprice())
    price_mootdx()
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

