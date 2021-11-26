#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

#Data is stored in directory data_modules
path="./data_modules/"

#read the data using read_csv
apple_price_data=pd.read_csv(path+"AAPL.csv",index_col=0)

#set the index to datetime object
apple_price_data.index=pd.to_datetime(apple_price_data.index)

#Display the last five rows
apple_price_data.tail()
#
#Display the concise summary of data
apple_price_data.info()
 
#Display the count of null values
apple_price_data.isna().sum()

#Drop the missing values
apple_price_data.dropna(inplace=True)

#Print the number of rows in dataframe
print("Number of rows:",apple_price_data.shape[0])

#Display the count of null values
apple_price_data.isna().sum()

#Display the count of duplicate values
print(apple_price_data.duplicated().value_counts)
print('Proportion of duplicate values is {}'.format( round(apple_price_data.duplicated().value_counts()[1]/apple_price_data.shape[0],4)))

#Drop the consecutive duplicate values
apple_price_data=apple_price_data.loc[(apple_price_data['close'].diff() != 0)|
                                      (apple_price_data['open'].diff() != 0) |
                                      (apple_price_data['high'].diff() != 0) |
                                      (apple_price_data['low'].diff() != 0) ]

#Check the number of rows
print("Number of rows:",apple_price_data.shape[0])

#Calculate the percentage change
apple_price_data['returns']=apple_price_data['close'].pct_change()
#     
#plot the percentage change
plt.figure(figsize=(10,7))
apple_price_data['returns'].plot()
#Set the title and axes label
plt.title('Returns',fontsize=14)
plt.xlabel('Year',fontsize=12)
plt.ylabel('Percent Change',fontsize=12)
#Show the plot
plt.show() 