#section 2.1

#for data manipulation
import pandas as pd 
#to fetch financial data
import yfinance as yf 
#for visualisation
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

#download apple data
# set ticker as "AAPL"
price_data_apple=yf.download("AAPL",start="2021-01-01")
#set index to a datetime object
price_data_apple.index=pd.to_datetime(price_data_apple.index)
#display first five rows
print(price_data_apple.tail())


#
#adjusted price data
price_data_apple_adjusted=yf.download("AAPl",start="2021-01-01",end="2021-05-20",auto_adjust=True)
#set index to a datetime object
price_data_apple_adjusted.index=pd.to_datetime(price_data_apple_adjusted.index)
#display first five rows
print(price_data_apple_adjusted.tail())
#
#
#
#plot the close price
plt.figure(figsize=(10,7))
price_data_apple_adjusted['Close'].plot()
#set the title and axes label
plt.title('Apple price data',fontsize=14)
plt.xlabel('Year-Month',fontsize=12)
plt.ylabel("Price",fontsize=12)
#show the plot
plt.show()
