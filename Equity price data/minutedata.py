#section 2.3
#for data manipulation
import pandas as pd 
#to fetch financial data
import yfinance as yf 
#for visualisation
import matplotlib.pyplot as plt
from yfinance import tickers
plt.style.use('seaborn-darkgrid')

#download minute data for apple
apple_minut_data=yf.download(tickers="AAPL",period="1d",interval="1m",auto_adjust='True')
#set index to datetime object
apple_minut_data.index=pd.to_datetime(apple_minut_data.index)
#display the first 5 rows
print("1 minute data")
print(apple_minut_data.head())

#resampling data
#aggregate function
ohlcv_dict={
            'Open':'first',
            'High':'max',
            'Low':'min',
            'Close':'last',
            'Volume':'sum'
}

#resampling to 15 minute data
#for 1hour use '1H'
apple_minut_data_15m=apple_minut_data.resample('15T').agg(ohlcv_dict)
#drop the missing values
apple_minut_data_15m.dropna(inplace=True)
#display first five rows
print("15 minute data")
print(apple_minut_data_15m.head())
