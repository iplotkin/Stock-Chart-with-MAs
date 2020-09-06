from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pyEX
import os
# from os.path import join, dirname
import dotenv

dotenv.load_dotenv()
# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)


API = os.getenv('API')

p = pyEX.Client(API)
ticker = 'TSLA'
timeframe = '1y'

df = p.chartDF(ticker, timeframe) # retrieve ticker data as a dataframe and store as df
df = df[['close']] # want chart to be based off close price
df.reset_index(level=0, inplace=True)
df.columns=['ds','pri']

sma50 = df.pri.rolling(window=50).mean() # 50 day simple moving average
sma200 = df.pri.rolling(window=200).mean() # 200 day simple moving average
ema20 = df.pri.ewm(span=20, adjust=False).mean() # 20 day EMA

plt.plot(df.ds, df.pri, label=ticker, color = 'black') # Plots the price chart of the ticker
plt.plot(df.ds, sma50, label='SMA(50) ' + str(sma50), color = 'blue')
plt.plot(df.ds, sma200, label='SMA(200) ' + str(sma200), color = 'red')
plt.plot(df.ds, ema20, label='EMA(20) ' + str(ema20), color = 'green')
plt.legend(loc='upper left')


plt.show()





# # prints key stats about the ticker
# stats = p.keyStats(ticker)
# for i in stats:
#     print(i, ": ", stats[i], sep="")
