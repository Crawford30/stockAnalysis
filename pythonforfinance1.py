import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2016, 12, 31)

ticker_dict = {}
for idx, ticker in enumerate(['TSLA']):
    try:
        df_ticker = web.DataReader(ticker, 'yahoo', start, end)
        ticker_dict[ticker] = df_ticker['Close']
    except:
        pass
stocks = pd.DataFrame(ticker_dict)

print(stocks.tail())
