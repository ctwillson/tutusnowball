import pysnowball as ball
import pandas as pd
import tushare as ts
import os
import threading
import time
import datetime
import argparse

dir_path = os.path.dirname(os.path.abspath(__file__))

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
    parser.add_argument('--mt', required=False, action='store_true',
                        help='wheather using multi threading')
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
    df.to_csv(dir_path + '/testdata/xueqiu/'+ts_code[0:6]+'.csv',encoding='utf8')

def get_historymin_price(ts_code,trade_timestamp,trade_datetime):

    print(ts_code[-2:]+ts_code[0:6])
    symbol = ts_code[-2:]+ts_code[0:6]
    min_path = dir_path + '/testdata/xueqiu/min/'+symbol+'/'
    if(not os.path.exists(min_path)):
        os.makedirs(min_path)
    for index,timestamp in enumerate(trade_timestamp):
        print(timestamp)
        data = ball.history_kline(symbol=symbol,begin=str(timestamp),period='1m',count=249)
        # print(data)
        # with open ('test.txt','a') as f:
        #     f.write(json.dumps(data))
        name = data['data']['column']
        coredata = data['data']['item']
        df = pd.DataFrame(columns=name,data=coredata)
        del df['volume_post']
        del df['amount_post']
        convert_datetime = lambda x: pd.to_datetime(str(x),utc=True,unit='ms').tz_convert(
                    "Asia/Shanghai")
        df['timestamp'] = df['timestamp'].apply(convert_datetime)

        bt_col_dict = {'timestamp':'datetime'}
        df = df.rename(columns = bt_col_dict)
        df = df.set_index('datetime')

        df.to_csv(min_path+trade_datetime[index]+'.csv',encoding='utf8')

def get_realtimemin_price(ts_code):
    print(ts_code[-2:]+ts_code[0:6])
    symbol = ts_code[-2:]+ts_code[0:6]
    data = ball.history_realtime_minute(symbol=symbol)
    # print(data)
def get_data(args):
    ts_token = os.getenv('TS_TOKEN')
    print('ts_token = ' + ts_token)

    ts.set_token(ts_token)
    pro = ts.pro_api()
    sotck_list = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    if  sotck_list.empty:
        print('get stock list failed,return!')
        exit()
    sotck_list.to_csv(dir_path + '/testdata/stocklist.csv')
    stock_name = sotck_list['ts_code']
    catdt_list = []
    caltimestamp_list = []
    trade_date = pro.trade_cal(exchange='', start_date='20210101', end_date='20210226')
    for index,row in trade_date.iterrows():
        if row['is_open'] == 1:
            dt = datetime.datetime.strptime(row['cal_date'], "%Y%m%d")
            catdt_list.append(str(dt)[0:10])
            dt = int(time.mktime(dt.timetuple()))*1000
            caltimestamp_list.append(dt)
    # print(cal_list)
    # stock_name = stock_name.tail(1443)
    if(args.all):
        for ts_code in stock_name:
            while True:
                try:
                    if(args.mt):
                        t1 = threading.Thread(target=get_exright_price, args=(ts_code,))
                        t1.start()
                    else:
                        get_exright_price(ts_code)
                    time.sleep(0.2)
                except:
                    print(ts_code + "failed")
                    time.sleep(2)
                    continue
                break
    else:
        # get_realtimemin_price(args.s)
        get_historymin_price(args.s,trade_timestamp=caltimestamp_list,trade_datetime = catdt_list)


if __name__ == '__main__':
    args = parse_args()
    get_data(args)
