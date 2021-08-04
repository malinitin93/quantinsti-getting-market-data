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
#
from fredapi import Fred
fred=Fred(get_fred_api())

# Get the 3 month, 1 year and 10 year treasury rates
# Series ID for Treasury Rates: DGS3MO, DGS1, DGS10
treasury_3M=fred.get_series('DGS3MO')
treasury_1Y=fred.get_series('DGS1')
treasury_10Y=fred.get_series('DGS10')
# Store the last value in 'macro_data'
macro_data['3 Month US Treasury'] = "{}%".format(treasury_3M[-1])
macro_data['1 Year US Treasury'] ="{}%".format(treasury_1Y[-1])
macro_data['10 Year US Treasury']="{}%".format(treasury_10Y[-1])
#plot the treasury rates
plt.figure(figsize=(15,7))
treasury_3M.plot(label='3 Month',alpha=0.5)
treasury_1Y.plot(label='1 Year',color='red',alpha=0.5)
treasury_10Y.plot(label='10 Year',color='green',alpha=0.5)
#set the title and axis label
plt.title('US treasury Rate',fontsize=12)
plt.xlabel('Date',fontsize=12)
plt.ylabel('Percentage',fontsize=12)
plt.legend()
#show the plot
plt.show()