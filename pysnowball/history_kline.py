from pysnowball import api_ref
from pysnowball import utls

def history_kline(symbol='SZ000001',begin='1502035200000',period='day',type='next',count='1000',indicator='kline'):
    url = api_ref.history_kline
    query = {
        'symbol': symbol,
        'begin': begin,
        'period': period,
        'type': type,
        'count': count,
        'indicator': indicator
    }
    return utls.fetch_with_login(url,query)
