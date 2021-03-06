#import libraries
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date
plt.style.use('seaborn-darkgrid')
import os
import sys
sys.path.append("..")
# edit fmda
from data_modules.FMDA_quantra import get_fred_api
macro_data=pd.DataFrame(index=['Value as of'+str(date.today())])
#
from fredapi import Fred
fred=Fred(get_fred_api())

#get the gold price
gold_price=yf.download('GLD','2018-01-01')['Close']
#Store the last value in macro data
macro_data['GLD Price']="{} USD".format(round(gold_price[-1],2))
#plot the gold price
plt.figure(figsize=(15,7))
gold_price.plot(color="red")
#set the title and axis label
plt.title('Gold Price',fontsize=14)
plt.xlabel('Year',fontsize=12)
plt.ylabel('USD',fontsize=12)
#show the plot
plt.show()
