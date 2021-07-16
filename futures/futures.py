#import the library to get data from yfinance
import yfinance as yf
#import matplotlib and set style for plotting
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

#
futures_data=yf.download(tickers="MSFT=F",start="2021-06-01",end="2021-06-24" ,threads=True)

#plot the adjusted close price
futures_data['Adj Close'].plot(figsize=(8,6))

#set the title and label for plot
plt.title('Lean Hog Continuous Future Adjusted Close Price',fontsize=12)
plt.xlabel('Year Month',fontsize=12)
plt.ylabel('Price',fontsize=12)
plt.show()
#
#
