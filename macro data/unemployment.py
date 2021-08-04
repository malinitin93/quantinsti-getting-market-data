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

#get the unemployment rate
# Series ID for Unemployment Rate: UNRATE
unemployment_rate=fred.get_series('UNRATE')
#store the last value in macro data
macro_data['Unemployment Rate']="{}%".format(unemployment_rate[-1])
#plot the unemployment rate
plt.figure(figsize=(15,7))
unemployment_rate.plot(color='orange')
#set the title and axis label
plt.title('Unemployment Rate',fontsize=14)
plt.xlabel('Date',fontsize=12)
plt.ylabel('Percent',fontsize=12)
plt.legend()
#show the plot
plt.show()