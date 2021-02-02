from pysnowball import api_ref
from pysnowball import utls

def private_pick(symbols):
    url = api_ref.private_pick
    return utls.post_formdata(url,symbol=symbols)