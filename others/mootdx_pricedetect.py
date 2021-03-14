from mootdx.quotes import Quotes
import pandas as pd
# while True:
client = Quotes.factory(market='std') 
client.quotes(symbol=["000001", "600300"]).to_csv('./quotes.csv')