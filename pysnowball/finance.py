import json
import os
from pysnowball import cons
from pysnowball import api_ref
from pysnowball import utls

import pandas as pd
import time


def cash_flow(symbol, is_annals=1, count=5):

    url = api_ref.finance_cash_flow_url+symbol
    
    if is_annals == 1:
        url = url + '&type=Q4'
    
    url = url + '&count='+str(count)

    return utls.fetch(url)