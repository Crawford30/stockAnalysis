import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

#column manipulation
#adding new column of moving averages
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
#df.dropna(inplace=True)
print(df.head())

#subplots are called axis
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()



# start = dt.datetime(2000, 1, 1)
# end = dt.datetime(2016, 12, 31)

# ticker_dict = {}
# for idx, ticker in enumerate(['TSLA', 'IBM', 'LNKD']):
#     try:
#         df_ticker = web.DataReader(ticker, 'yahoo', start, end)
#         ticker_dict[ticker] = df_ticker['Close']
#     except:
#         pass
# stocks = pd.DataFrame(ticker_dict)
#
# print(stocks.tail())
