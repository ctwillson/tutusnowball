from http.cookiejar import Cookie
import requests
import json

import pysnowball.cons as cons
import pysnowball.token as token
import aiohttp
import asyncio

async def fetch_async(url):
    HEADERS = {'Host': 'stock.xueqiu.com',
               'Accept': 'application/json',
               'Cookie': token.get_token(),
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
               'Accept-Language': 'zh-Hans-CN;q=1, ja-JP;q=0.9',
               'Accept-Encoding': 'br, gzip, deflate',
               'Connection': 'keep-alive'}
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url,headers=HEADERS) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html, "...")

def fetch(url,is_async = False):
    HEADERS = {'Host': 'stock.xueqiu.com',
               'Accept': 'application/json',
               'Cookie': token.get_token(),
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
               'Accept-Language': 'zh-Hans-CN;q=1, ja-JP;q=0.9',
               'Accept-Encoding': 'br, gzip, deflate',
               'Connection': 'keep-alive'}
    if(is_async):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(fetch_async(url))
    response = requests.get(url,headers=HEADERS)

    # print(url)
    # print(HEADERS)
    # print(response)
    # print(response.content)

    if response.status_code != 200:
        raise Exception(response.content)

    return json.loads(response.content)
# TODO:try to automaticly login to get cookie
def fetch_with_login(url,query,is_async = False):
    HEADERS = {'Host': 'stock.xueqiu.com',
               'Accept': 'application/json',
               'Cookie': 'put your cookie!!!',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
               'Accept-Language': 'zh-Hans-CN;q=1, ja-JP;q=0.9',
               'Accept-Encoding': 'br, gzip, deflate',
               'Connection': 'keep-alive'}
    if(is_async):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(fetch_async(url))
    response = requests.get(url,params=query,headers=HEADERS)

    if response.status_code != 200:
        raise Exception(response.content)

    return json.loads(response.content)

def fetch_without_token(url):
    HEADERS = {'Host': 'stock.xueqiu.com',
               'Accept': 'application/json',
               'User-Agent': 'Xueqiu iPhone 11.8',
               'Accept-Language': 'zh-Hans-CN;q=1, ja-JP;q=0.9',
               'Accept-Encoding': 'br, gzip, deflate',
               'Connection': 'keep-alive'}

    response = requests.get(url, headers=HEADERS)

    # print(url)
    # print(HEADERS)
    # print(response)
    # print(response.content)

    if response.status_code != 200:
        raise Exception(response.content)

    return json.loads(response.content)

def post_formdata(url,symbol):
    HEADERS = {'Host': 'stock.xueqiu.com',
            'Accept': 'application/json',
            'Cookie': 'put your cookie!!!',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'Accept-Language': 'zh-Hans-CN;q=1, ja-JP;q=0.9',
            'Accept-Encoding': 'br, gzip, deflate',
            'Connection': 'keep-alive'}
    post_data = {'symbols':symbol}
    response = requests.post(url = url,data=post_data,headers = HEADERS)
    print(response.text)