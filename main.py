from bs4 import BeautifulSoup
import yfinance as yf
import pandas as pd

apple = yf.Ticker("AAPL")
apple_info = apple.info
print(apple_info['country'])
apple_share_price_data = apple.history(period="max")
apple_share_price_data.head()
amd = yf.Ticker('AMD')
amd_info = amd.info
print(amd_info)
amd_history = amd.history(period="max")
print(amd_history['Volume'])
amd_volume = amd_history["Volume"]
list = []
for vol in amd_volume:
    list.append(vol)
list.sort()
print(list)
print(list[-1])













