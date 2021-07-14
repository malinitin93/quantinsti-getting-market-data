#import yfinance package
import yfinance as yf

#for plotting
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

#create ticker object for microsoft
msft=yf.Ticker('MSFT')

#call the options on ticker object to get expiration dates
msft.options()

# Get options chain for specific expiration date
option_chain=msft.option_chain(date=msft.options[0])

#get microosft call option chain data
option_chain.calls.head()

#plot the call strike price vs call last traded price
plt.figure(figsize=(15,7))
plt.plot(option_chain.calls.strike,option_chain.calls.lastPrice)
plt.xlabel('Strike Price',fontSize=12)
plt.ylabel('Last Price',fontSize=12)
plt.title('Microsoft call options for Different Strike Price',fontSize=14)
plt.show()


##
##
##
#get Microsoft Put Options chain data
option_chain.puts.head()
#plot the put strike price vs put last traded price
plt.figure(figsize=(15,7))
plt.plot(option_chain.puts.strike,option_chain.puts.lastPrice)
plt.xlabel('Strike Price',fontSize=12)
plt.ylabel('Last Price',fontSize=12)
plt.title('Microsoft put options for different Strike Price',fontSize=14)
plt.show()

