#section 2.2
#for data manipulation
import pandas as pd 
#to fetch financial data
import yfinance as yf 

#url of the source
url=""
#read and print stock tickers
tickers=pd.read_html(url)[0]
tickers.head()

#convert ticker to list
ticker_symbol=tickers['Symbol'].tolist()
#clean symbols
ticker_symbol=[ticker.replace(".","-")for ticker in ticker_symbol]

#get data from yfinance
data=yf.download(ticker_symbol,'2021-05-01',auto_adjust=True)['Close']
print(data.head())