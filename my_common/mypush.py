# encoding:utf-8
from pysnowball import token
import requests
import json
import os

def get_token():
    if os.getenv('PUSHPLUSTOKEN') is None:
        raise Exception('pushplus token not set!')
    else:
        return os.getenv('PUSHPLUSTOKEN')
token = get_token()
def pushplus(title,content):
    # title= title #改成你要的标题内容
    # content ='https://baike.baidu.com/item/www/109924?fr=aladdin' #改成你要的正文内容
    url = 'http://pushplus.hxtrip.com/send?token='+token+'&title='+title+'&content='+content
    requests.get(url)

def pushplus_group(title,content,code):
    url = 'http://pushplus.hxtrip.com/send'
    data = {
        "token": token,
        "title": str(title),
        "content": str(content),
        "topic": str(code),
        "template":"html"
    }
    #print(data)
    body=json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type':'application/json'}
    requests.post(url,data=body,headers=headers)