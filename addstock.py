import pysnowball as ball
import time
with open('./testdata/stock/test.txt', 'r') as file_object:
    stock_list = file_object.readlines()
for name in stock_list:
    symbol = name[-3:-1]+name[11:17]
    print(symbol)
    ball.private_pick(symbol)
    ball.private_packet(symbols=symbol,packet_name='test')
    time.sleep(0.1)