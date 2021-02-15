import os
import pysnowball.cons as cons
import requests

def get_cookie():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    url = 'https://xueqiu.com/'

    response = requests.get(url = url,headers=headers)
    dic_cookie = requests.utils.dict_from_cookiejar(response.cookies)
    return dic_cookie['xq_a_token']

def get_token():
    if os.environ.get('XUEQIUTOKEN') is None:
        raise Exception(cons.NOTOKEN_ERROR_MSG)
    else:
        return os.environ['XUEQIUTOKEN']

def get_login_token():
    if os.getenv('XUEQIULOGINCOOKIE') is None:
        raise Exception(cons.NOTOKEN_ERROR_MSG)
    else:
        return os.getenv('XUEQIULOGINCOOKIE')

def set_token():
    os.environ['XUEQIUTOKEN'] = 'xq_a_token=' + get_cookie()
    return os.environ['XUEQIUTOKEN']
