import json
import os
import asyncio
from pysnowball import cons
from pysnowball import api_ref
from pysnowball import utls


def quotec(symbol):
    url = api_ref.realtime_quote+symbol
    return utls.fetch(url)

async def quotec_async(symbol):
    url = api_ref.realtime_quote+symbol
    return await (utls.fetch_async(url))

def pankou(symbol):
    url = api_ref.realtime_pankou+symbol
    return utls.fetch_without_token(url)

