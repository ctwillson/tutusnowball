from pysnowball import api_ref
from pysnowball import utls

'''
type_name:
    - before: 前复权(split-adjusted?)
    - normal: 不复权
    - after: 后复权
'''
def history_kline(symbol='SZ000001',begin='1502035200000',period='day',type_name='before',count='1000',indicator='kline'):
    url = api_ref.history_kline
    query = {
        'symbol': symbol,
        'begin': begin,
        'period': period,
        'type': type_name,
        'count': count,
        'indicator': indicator
    }
    return utls.fetch_with_login(url,query)

def history_realtime_minute(symbol='SZ000001',period='1d'):
    url = api_ref.realtime_minute
    query = {
        'symbol': symbol,
        'period': period,
    }
    return utls.fetch_with_login(url,query)