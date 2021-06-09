#section 2.2

#for data manipulation
import pandas as pd 
#to fetch financial data
import yfinance as yf 
#for visualisation
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

#define ticker list
tickers_list=['AAPL','AMZN','MSFT']
#download data for above ticker
price_data=yf.download(tickers_list,start="2021-05-01")['Adj Close']
#set the index to determine object
price_data.index=pd.to_datetime(price_data.index)
#display first five rows
print(price_data.head())

#plot the series
plt.figure(figsize=(10,7))
(price_data['AAPL']/price_data['AAPL'].iloc[0]).plot()
(price_data['AMZN']/price_data['AAPL'].iloc[0]).plot()
(price_data['MSFT']/price_data['AAPL'].iloc[0]).plot()

#set the title and axes label
plt.title('Price in Change',fontsize=14)
plt.xlabel('Year-Month',fontsize=12)
plt.ylabel("Price Change",fontsize=12)
plt.legend()
#show the plot
plt.show()


