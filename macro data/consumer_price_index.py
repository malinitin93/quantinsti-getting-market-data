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
#
#
#consumer price index
#Get the CPI
#Series ID for CPI:CPIAUCSL
cpi=fred.get_series('CPIAUCSL')
#Store the last value in macro data
macro_data['CPI']="{}%".format(round(cpi.pct_change(periods=12)[-1],4)*100)
#plot the CPI
plt.figure(figsize=(15,7))
(cpi.pct_change(periods=12)*100).plot(color="brown")
#set the title and axis label
plt.title('CPI',fontsize=12)
plt.xlabel('DATE',fontsize=12)
plt.ylabel('Percent',fontsize=12)
#Show the plot
plt.show()