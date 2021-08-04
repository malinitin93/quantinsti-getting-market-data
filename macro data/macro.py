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
#get US GDP
#Series ID for US GDP:GDp
gdp=fred.get_series('GDP')
#Data is fetched into Billions USD, divide by 1000 to convert into Trillions
gdp=gdp/1000
#Store the last value in macro data
macro_data['US GDP']="{} trillions USD".format(gdp[-1])

#Plot the GDP
plt.figure(figsize=(15,7))
gdp.plot()
#Set the title and axis label
plt.title('GDP',fontsize=14)
plt.xlabel('Year',fontsize=12)
plt.ylabel('Trillions of Dollars',fontsize=12)
#show the plot
plt.show()

#
#GDP of different countries
import wbgapi as wb
ny_gdp=wb.data.DataFrame(['ny.gdp.mktp.cd'],mrv=1,labels=True).dropna().sort_values(by='NY.GDP.MKTP.CD',ascending=False)[:10]
print(ny_gdp)

#GDP of 6 countries in Trillions USD
GDP=wb.data.DataFrame(['ny.gdp.mktp.cd'],['USA','CHN','JPN','DEU','IND','GBR']).T.dropna()/(10**12)

#Plot the GDP
fig, ax=plt.subplots(figsize=(15,7))
xtick=[int(x[-4:]) for x in GDP.index.tolist()]
#plot  the series
ax.plot(xtick,GDP['USA'])
ax.plot(xtick,GDP['CHN'])
ax.plot(xtick,GDP['JPN'])
ax.plot(xtick,GDP['DEU'])
ax.plot(xtick,GDP['IND'])
ax.plot(xtick,GDP['GBR'])
 
#Set the title and axis label
plt.title('GDP',fontsize=14)
plt.xlabel('Year',fontsize=12)
plt.ylabel('Trillions of Dollars',fontsize=12)
plt.legend()
#show the plot
plt.show()

#
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

#
# Get the 3 month, 1 year and 10 year treasury rates
# Series ID for Treasury Rates: DGS3MO, DGS1, DGS10
treasury_3M=fred.get_series('DGS3MO')
treasury_1Y=fred.get_series('DGS1')
treasury_10Y=fred.get_series('DGS10')



