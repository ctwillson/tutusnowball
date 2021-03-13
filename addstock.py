import pysnowball as ball
import time
import os
import datetime
import sys
import pandas as pd
dir_path = os.path.dirname(os.path.abspath(__file__))
cal = str(datetime.date.today().strftime('%m%d'))

print(cal)
with open('./testdata/stock/attention.txt', 'r') as file_object:
    stock_list = file_object.readlines()
for symbol in stock_list:
    symbol = symbol[11:19]
    print(symbol)
    ball.private_pick(symbol)
    ball.private_packet(symbols=symbol,packet_name='zg'+cal)
    time.sleep(0.1)
# df = pd.read_csv(dir_path+'/testdata/attention/test.csv')
# stock_list = df.loc[:,'ts_code']
# price_zg = df.loc[:,'last_zg']
# for index,symbol in enumerate(stock_list):
#     down = price_zg[index] + 0.05
#     ball.price_alert(symbol=symbol,price_desc = down)