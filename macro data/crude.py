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
#get the US Brent Crude price
#Series ID for US Brent Crude Price:POILBREUSDM
us_brent_crude=fred.get_series('POILBREUSDM')
#Store the last value in macro data
macro_data['US Brent Crude']="{} USD Per Barrel".format(us_brent_crude[-1])

#Plot the Crude Price
plt.figure(figsize=(15,7))
plt.title('US Brent Crude $ per Barrel',fontsize=14)
plt.xlabel('Date',fontsize=12)
plt.ylabel('USD Per Barrel',fontsize=12)
plt.legend()
#show the plot
plt.show()
