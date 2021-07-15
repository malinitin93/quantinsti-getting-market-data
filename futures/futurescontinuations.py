#import matplotlib
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')
#data manipulation lib
import pandas as pd
#path to read data files
path="./data_modules/"

#read the data
#First Contract
first_contract_data=pd.read_csv( path+"HEV20.csv", index_col=0, parse_dates=True)
#Second Contract
second_contract_data=pd.read_csv(path+"HEZ20.csv", index_col=0, parse_dates=True)
#define the plot size
plt.figure(figsize=(8,6))
plt.title('Unadjusted Futures Price',fontsize=12)
plt.xlabel('Year-Month',fontsize=12)
plt.ylabel('Price',fontsize=12)

#plotting the first contract
plt.plot(first_contract_data.Settle,label='HEV20',color='orange')
#plotting the second contract after first contract expires
first_contract_expiry=first_contract_data.index.max()
plt.plot(second_contract_data.Settle.loc[first_contract_expiry:],label="HEZ20",color='green')

#Adding the legend
plt.legend()
#show the plot
plt.show()

#part-2
#
#Proportional adjustment
#First contract price
first_contract_on_expiry=first_contract_data.loc[first_contract_expiry].Settle

#Second contract price
second_contract_on_rollover=second_contract_data.loc[first_contract_expiry].Settle

#Proportional adjustment factor
adjustment_factor=\
    second_contract_on_rollover /first_contract_on_expiry

#Define variable to store continuous series
continuous_futures_proportional=pd.Series()

#Make the continous futures series without adjustment
continuous_futures_proportional=\
    continuous_futures_proportional.append(first_contract_data.loc[:first_contract_expiry].Settle)

#Multiply the adjustment factor to the continuous series till the expiry of the first contract
continuous_futures_proportional.loc[:first_contract_expiry] *=adjustment_factor

continuous_futures_proportional=\
    continuous_futures_proportional.append(second_contract_data.loc[first_contract_expiry:].Settle)

#Print the prices
print("The price of first contract on{} is ${}.".format(first_contract_expiry,first_contract_on_expiry))

print("The price of the second contract on {} is ${}".format(first_contract_expiry,second_contract_on_rollover))

print("The adjustment factor to multiply to the first contract is{}." .format(round(adjustment_factor,3)))

#Define the plot size
plt.figure(figsize=(8,7))
plt.title('Adjusted Futures Contracts', fontsize=14)
plt.xlabel('Year-Month',fontsize=12)
plt.ylabel('Price',fontsize=12)

#Plotting the continous contract
plt.plot(continuous_futures_proportional)

#show the plot
plt.show()