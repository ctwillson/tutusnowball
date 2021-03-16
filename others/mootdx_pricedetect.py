from mootdx.quotes import Quotes
import pandas as pd
# while True:
client = Quotes.factory(market='std') 
df = client.quotes(symbol=["000001", "600300"])
print(df.loc[:,'price'])