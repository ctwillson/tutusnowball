import akshare as ak
import pandas as pd
import os
dir_path = os.path.dirname(os.path.abspath(__file__))
sotck_list = pd.read_csv(dir_path + '/..'+'/testdata/stocklist.csv')
stock_name = sotck_list['ts_code']
for symbol in stock_name:
    name = symbol[-2:]+symbol[0:6]
    stock_zh_a_minute_df = ak.stock_zh_a_minute(symbol=name, period='1', adjust="qfq")
    min_path = dir_path + '/..'+'/testdata/akshare/min/'+name
    if(not os.path.exists(min_path)):
        os.makedirs(min_path)
    stock_zh_a_minute_df.to_csv(min_path+'/'+name+'.csv',encoding='utf8')
print(stock_zh_a_minute_df)