# import libraries
import cryptocompare
import pandas as pd
import datetime as datetime
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

#module to fetch cryptocompare data and api key
import sys   
sys.path.append("..")
from data_modules.FMDA_quantra import get_cryptocompare_api

#get the api key from data_modules folder
cryptocompare_API_key=get_cryptocompare_api()
#set api key in cryptocomapre object
cryptocompare.cryptocompare._set_api_key_parameter(cryptocompare_API_key)
print("API key is set")

#fetch the raw ticker list
raw_ticker_data=cryptocompare.get_coin_list()
#convert the raw data from dictionary format to DataFrame
all_tickers=pd.DataFrame.from_dict(raw_ticker_data).T

# last 5 entries
print(".......")
print(all_tickers.tail())

#bitcoin hourly data for 5th June 2021
#define ticker symbol and other details
ticker_symbol='BTC'
currency = 'USD'
limit_value = 2000
exchange_name = 'CCCAGG'
data_before_timestamp = datetime(2021, 6,5, 0, 0)
#fetch the raw price data
