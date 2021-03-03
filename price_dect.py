import json
import time
import pandas as pd
import asyncio
import pysnowball as ball
import my_common


# stock_list = ['SZ000001','SZ000004']
tasks = []
ball.set_token()
df = pd.read_csv('testdata/attention/test.csv')
stock_list = df['ts_code']
price_zg = df['last_zg']
async def getprice():
    for symbol in stock_list:
        print(symbol)
        tasks.append(asyncio.create_task(ball.quotec_async(str(symbol))))
    while(True):
        results = await asyncio.gather(*tasks)
        for data in results:
            data = json.loads(data)
            print(data['data']['quote']['current'])
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