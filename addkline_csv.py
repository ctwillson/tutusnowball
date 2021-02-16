import pysnowball as ball
import pandas as pd
import tushare as ts
import os
import threading
import time
import argparse

def parse_args(pargs=None):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description=(' - '.join([
            'BTFD',
            'http://dark-bid.com/BTFD-only-strategy-that-matters.html',
            ('https://www.reddit.com/r/algotrading/comments/5jez2b/'
             'can_anyone_replicate_this_strategy/')]))
        )
    parser.add_argument('--all', required=False, action='store_true',
                        help='run all a stock')

    parser.add_argument('--s', required=False, default='000001.SZ',
                        help='to test which stocks')
    return parser.parse_args(pargs)
def get_exright_price(ts_code):
    print(ts_code[-2:]+ts_code[0:6])
    symbol = ts_code[-2:]+ts_code[0:6]
    data = ball.history_kline(symbol=symbol)
    # print(data)
    # with open ('test.txt','a') as f:
    #     f.write(json.dumps(data))
    name = data['data']['column']
    coredata = data['data']['item']
    df = pd.DataFrame(columns=name,data=coredata)
    del df['volume_post']
    del df['amount_post']
    convert_datetime = lambda x: pd.to_datetime(str(x),utc=True,unit='ms').tz_convert(
                "Asia/Shanghai").to_period("D")
    df['timestamp'] = df['timestamp'].apply(convert_datetime)

    bt_col_dict = {'timestamp':'datetime'}
    df = df.rename(columns = bt_col_dict)
    df = df.set_index('datetime')
    df.to_csv('./testdata/day/'+ts_code[0:6]+'.csv',encoding='utf8')
def get_data(args):
    ts_token = os.getenv('TS_TOKEN')
    print('ts_token = ' + ts_token)

    ts.set_token(ts_token)
    pro = ts.pro_api()
    sotck_list = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    if  sotck_list.empty:
        print('get stock list failed,return!')
        exit()
    sotck_list.to_csv('./testdata/stocklist.csv')
    stock_name = sotck_list['ts_code']
    # stock_name = stock_name.tail(1443)
    if(args.all):
        for ts_code in stock_name:
            while True:
                try:
                    t1 = threading.Thread(target=get_exright_price, args=(ts_code,))
                    t1.start()
                    time.sleep(0.2)
                except:
                    print(ts_code + "failed")
                    time.sleep(2)
                    continue
                break
    else:
        get_exright_price(args.s)


if __name__ == '__main__':
    args = parse_args()
    get_data(args)
