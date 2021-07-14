#import lib
import pandas as pd
import numpy as np

#import get history function from nsepy module
from nsepy import get_history

#for manuplatinf date
from datetime import date

#for plotting
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

#Get options data for Nifty index
nifty_options =get_history(
                            symbol='Nifty',
                            start=date(2021,7,8),
                            end=date(2021,7,14),
                            index=True,
                            expiry_date=date(2021,7,15),
                            option_type='CE',
                            Strike_Price=15500
                          )
nifty_options.head()
#
#
#
fig=plt.figure(figSize=(15,10))
#plot close prices
ax=fig.add_subplot(211)
ax.plot(nifty_options['Close'])
ax.setTitle('15500 Strike NIFTY Call Close Price',fontsize=14)
ax.set_ylabel('Close Price',fontsize=12)
ax.set_xlabel('Date',fontsize=12)
#
#
#plot the cumulative returns
ax=fig.add_subplot(211)
ax=nifty_options['Open Interest'].plot(kind='bar',color='c')
ax.set_title('15500 Strike Nifty call Open Interest',fontsize=14)
ax.set_ylabel('Open Interest',fontsize=12)
ax.set_xlabel('Date',fontsize=12)

plt.show()

