import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mplfinance.original_flavor import candlestick_ohlc
#from matplotlib.finance import candletstick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)


#adding new column of moving averages
#df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()


ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

#resampling data incase of taking secondly data I would use daily data

#Two steps involved, create new data frame and

#takes the mean after every ten days, resample('10D').mean(), or resample('10D').ohlc() open high low close
df_ohlc  = df['Adj Close'].resample('10D').ohlc()

df_volume = df['Volume'].resample('10D').sum()

#modfying date to matplotlib date
df_ohlc.reset_index(inplace=True)

#convert dates to mdate
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

#print(df_ohlc.head())


#subplots are called axis
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date() #take mdates and convert to nice display

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')

ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values,0) #fill from 0 to the y ie df_volume.values,0



plt.show()