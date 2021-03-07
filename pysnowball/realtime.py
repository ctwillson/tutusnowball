import json
import os
import asyncio

from requests.sessions import session
from pysnowball import cons
from pysnowball import api_ref
from pysnowball import utls


def quotec(symbol):
    url = api_ref.realtime_quote+symbol
    return utls.fetch(url)

async def quotec_async(symbol,sem,session):
    url = api_ref.realtime_quote+symbol
    async with sem:
        return await (utls.fetch_async(url,session))

def pankou(symbol):
    url = api_ref.realtime_pankou+symbol
    return utls.fetch_without_token(url)

