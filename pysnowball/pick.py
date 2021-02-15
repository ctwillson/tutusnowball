from pysnowball import api_ref
from pysnowball import utls

def private_pick(symbols='SZ000001'):
    url = api_ref.private_pick
    post_data = {'symbols':symbols}
    return utls.post_formdata(url,post_data=post_data)

def private_packet(symbols='SZ000001',packet_name='test',category=1):
    url = api_ref.private_packet
    post_data = {
        'symbols': symbols,
        'pnames': packet_name,
        'category': category,
    }
    return utls.post_formdata(url,post_data=post_data)