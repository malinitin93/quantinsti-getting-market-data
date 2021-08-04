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