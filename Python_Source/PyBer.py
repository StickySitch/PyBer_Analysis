#!/usr/bin/env python
# coding: utf-8

# In[125]:


get_ipython().run_line_magic('matplotlib', 'inline')
#import dependencies
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as sts
import matplotlib as mpl

#Instantiate locations of data files
cityData = 'Resources/city_data.csv'
rideData = 'Resources/ride_data.csv'

#Reading city_data.csv to a DataFrame
cityDf = pd.read_csv(cityData)
cityDf.head(10)


# In[126]:


#Reading ride_data.csv to a DataFrame
rideDf = pd.read_csv(rideData)
rideDf.head(10)


# In[127]:


#checking for missing values
cityDf.count()


# In[128]:


#Checking for missing values
cityDf.isnull().sum()


# In[129]:


#Checking data types
cityDf.dtypes


# In[130]:


#Getting the different city types
cityDf['type'].unique()


# In[131]:


#Getting the count of "Urban" data points
sum(cityDf['type']=='Urban')


# In[132]:


#Getting the count of "Rural" data points
sum(cityDf['type']=='Rural')


# In[133]:


#Getting the count of "Suburban" data points
sum(cityDf['type']=='Suburban')


# In[134]:


#Checking rideDf for missing values
rideDf.count()


# In[135]:


#Checking rideDf for missing values
rideDf.isnull().sum()


# In[136]:


#Checking rideDf data types
rideDf.dtypes


# In[137]:


#Combining the data into a single dataset
pyberDataDf = pd.merge(rideDf, cityDf, how='left', on=['city','city'])
pyberDataDf.head(10)


# In[138]:


#Creating Urban city DataFrame
urbanCitiesDf = pyberDataDf[pyberDataDf['type']=='Urban']
#Creating Rural city DataFrame
ruralCitiesDf = pyberDataDf[pyberDataDf['type']=='Rural']
#Creating Suburban city DataFrame
subCitiesDf = pyberDataDf[pyberDataDf['type']=='Suburban']


# In[139]:


# Getting the number of rides for urban cities.
urbanRideCount = urbanCitiesDf.groupby(['city']).count()['ride_id']
subRideCount = subCitiesDf.groupby(['city']).count()['ride_id']
ruralRideCount = ruralCitiesDf.groupby(['city']).count()['ride_id']
urbanRideCount.head()


# In[140]:


# Getting average fare for each city in the urban cities.
urbanAvgFare = urbanCitiesDf.groupby(['city']).mean()['fare']
ruralAvgFare = ruralCitiesDf.groupby(['city']).mean()['fare']
subAvgFare = subCitiesDf.groupby(['city']).mean()['fare']
urbanAvgFare.head()


# In[141]:


urbanDriverCount = urbanCitiesDf.groupby(['city']).mean()['driver_count']
ruralDriverCount = ruralCitiesDf.groupby(['city']).mean()['driver_count']
subDriverCount = subCitiesDf.groupby(['city']).mean()['driver_count']
urbanDriverCount.head()


# In[142]:


# Building the scatter plots for urban cities.
plt.scatter(urbanRideCount, urbanAvgFare, 
            s=10*urbanDriverCount, c='coral', 
            edgecolor='black',linewidths=1,
            alpha=0.8, label='urban')
plt.title('PyBer Ride-Sharing Data (2019)')
plt.ylabel('Average Fare ($)')
plt.xlabel('Total Number of Rides (Per City)')
plt.grid(True)
plt.legend()


# In[143]:


# Building the scatter plots for suburban cities.
plt.scatter(subRideCount, subAvgFare, 
            s=10*subDriverCount, c='skyblue', 
            edgecolor='black',linewidths=1,
            alpha=0.8, label='Suburban')
plt.title('PyBer Ride-Sharing Data (2019)')
plt.ylabel('Average Fare ($)')
plt.xlabel('Total Number of Rides (Per City)')
plt.grid(True)
plt.legend()


# In[144]:


# Building the scatter plots for rural cities.
plt.scatter(ruralRideCount, ruralAvgFare, 
            s=10*ruralDriverCount, c='gold', 
            edgecolor='black',linewidths=1,
            alpha=0.8, label='Rural')
plt.title('PyBer Ride-Sharing Data (2019)')
plt.ylabel('Average Fare ($)')
plt.xlabel('Total Number of Rides (Per City)')
plt.grid(True)
plt.legend()


# In[145]:


# Building the scatter plots for urban cities.
plt.subplots(figsize=(10,6))
plt.scatter(urbanRideCount, urbanAvgFare, 
            s=10*urbanDriverCount, c='coral', 
            edgecolor='black',linewidths=1,
            alpha=0.8, label='urban')


# Building the scatter plots for suburban cities.
plt.scatter(subRideCount, subAvgFare, 
            s=10*subDriverCount, c='skyblue', 
            edgecolor='black',linewidths=1,
            alpha=0.8, label='Suburban')



# Building the scatter plots for rural cities.
plt.scatter(ruralRideCount, ruralAvgFare, 
            s=10*ruralDriverCount, c='gold', 
            edgecolor='black',linewidths=1,
            alpha=0.8, label='Rural')

plt.title('PyBer Ride-Sharing Data (2019)')
plt.ylabel('Average Fare ($)')
plt.xlabel('Total Number of Rides (Per City)')
plt.grid(True)
# Create a legend
lgnd = plt.legend(fontsize="12", mode="Expanded",
         scatterpoints=1, loc="best", title="City Types")
lgnd.legendHandles[0]._sizes = [75]
lgnd.legendHandles[1]._sizes = [75]
lgnd.legendHandles[2]._sizes = [75]
lgnd.get_title().set_fontsize(12)
plt.text(42,35, "Note: Circle size correlates with driver count per city.", fontsize="12")
#saving the figure
plt.savefig('Analysis/Fig1.png')
plt.show()


# In[146]:


# Getting statistical info of urban cities
urbanCitiesDf.describe()


# In[147]:


# Getting statistical info of rural cities
ruralCitiesDf.describe()


# In[148]:


# Getting statistical info of suburban cities
subCitiesDf.describe()


# In[149]:


# Getting statistical info of urban cities ride count data
urbanRideCount.describe()


# In[150]:


# Getting statistical info of rural cities ride count data
ruralRideCount.describe()


# In[151]:


# Getting statistical info of suburban cities ride count data
subRideCount.describe()


# In[152]:


#Calculating the average ride count for each city type
round(urbanRideCount.mean(),2), round(subRideCount.mean(),2), round(ruralRideCount.mean(),2)


# In[153]:


#Calculating the median ride count for urban cities
round(urbanRideCount.median(),2)


# In[154]:


# Calculating the mode of the ride count for the urban cities.
urbanRideCount.mode()


# In[155]:


# Calculating the mode of the ride count for the suburban cities.
subRideCount.mode()


# In[156]:


# Calculating the mode of the ride count for the rural cities.


# In[157]:


ruralRideCount.mode()


# In[158]:


# Calculating the measures of central tendency for the ride count for the urban cities.
meanUrbanRideCount = np.mean(urbanRideCount)
print(f'The mean for the ride counts for urban trips is {meanUrbanRideCount:.2f}')

medianUrbanRideCount = np.median(urbanRideCount)
print(f'The median for the ride counts for urban trips is {medianUrbanRideCount:.2f}')

modeUrbanRideCount = sts.mode(urbanRideCount)
print(f'The median for the ride counts for urban trips is {modeUrbanRideCount}.')


# In[159]:


modeSubRideCount = sts.mode(subRideCount)
print(f'The median for the ride counts for urban trips is {modeSubRideCount}.')


# In[160]:


modeRuralRideCount = sts.mode(ruralRideCount)
print(f'The median for the ride counts for urban trips is {modeRuralRideCount}.')


# In[161]:


# Getting the fares for the urban cities.
urbanFares = urbanCitiesDf['fare']
urbanFares.head()


# In[162]:


meanUrbanFares = np.mean(urbanFares)
print(f'The mean for the urban fares is ${meanUrbanFares:.2f}')

medianUrbanFares = np.median(urbanFares)
print(f'The median for the urban fares is ${medianUrbanFares:.2f}')

modeUrbanFares = sts.mode(urbanFares)
print(f'The mode for the urban fares is {modeUrbanFares}')


# In[163]:



ruralFares = ruralCitiesDf['fare']


meanRuralFares = np.mean(ruralFares)
print(f'The mean for the rural fares is ${meanRuralFares:.2f}')

medianRuralFares = np.median(ruralFares)
print(f'The median for the rural fares is ${medianRuralFares:.2f}')

modeRuralFares = sts.mode(ruralFares)
print(f'The mode for the rural fares is {modeRuralFares}')


# In[164]:


subFares = subCitiesDf['fare']

meanSubFares = np.mean(subFares)
print(f'The mean for the sub fares is ${meanSubFares:.2f}')

medianSubFares = np.median(subFares)
print(f'The median for the sub fares is ${medianSubFares:.2f}')

modeSubFares = sts.mode(subFares)
print(f'The mode for the sub fares is {modeSubFares}')


# In[165]:


#Creating series of each cities driver count
urbanDrivers = urbanCitiesDf['driver_count']
ruralDrivers = ruralCitiesDf['driver_count']
subDrivers = subCitiesDf['driver_count']
urbanDrivers.head()


# In[166]:


#Calculations for driver count by urban city type

meanUrbanDrivers = np.mean(urbanDrivers)
print(f'The mean for the urban driver count is {meanUrbanDrivers:.2f}')

medianUrbanDrivers = np.median(urbanDrivers)
print(f'The median for the urban driver count is {medianUrbanDrivers:.2f}')

modeUrbanDrivers = sts.mode(urbanDrivers)
print(f'The mode for the urban driver count is {modeUrbanDrivers}')


# In[167]:


#Calculations for driver count by rural city type

meanRuralDrivers = np.mean(ruralDrivers)
print(f'The mean for the rural driver count is {meanRuralDrivers:.2f}')

medianRuralDrivers = np.median(ruralDrivers)
print(f'The median for the rural driver count is {medianRuralDrivers:.2f}')

modeRuralDrivers = sts.mode(ruralDrivers)
print(f'The mode for the rural driver count is {modeRuralDrivers}')


# In[168]:


#Calculations for driver count by suburban city type

meanSubDrivers = np.mean(subDrivers)
print(f'The mean for the sub driver count is {meanSubDrivers:.2f}')

medianSubDrivers = np.median(subDrivers)
print(f'The median for the sub driver count is {medianSubDrivers:.2f}')

modeSubDrivers = sts.mode(subDrivers)
print(f'The mode for the sub driver count is {modeSubDrivers}')


# In[169]:


# Creating a box-and-whisker plot for the urban cities ride count.
xLabels = ['Urban']
fig, ax = plt.subplots()
ax.boxplot(urbanRideCount, labels=xLabels)
#Adding title, labels and grid
ax.set_title('Ride Count Data (2019)')
ax.set_ylabel('Number Of Rides')
ax.set_yticks(np.arange(10,41, step=2.0))
ax.grid()
plt.show()


# In[170]:


# Add all ride count box-and-whisker plots to the same graph.
xLabels = ['Urban','Suburban','Rural']
rideCountData = [urbanRideCount, ruralRideCount, subRideCount]

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title('Ride Count Data (2019)',fontsize=20)
ax.set_ylabel('Number of Rides',fontsize=14)
ax.set_xlabel('City Types',fontsize=14)
ax.boxplot(rideCountData, labels=xLabels)
ax.set_yticks(np.arange(0,45, step=3.0))
ax.grid()
#saving figure
plt.savefig('Analysis/Fig2.png')
plt.show()


# In[171]:


# Getting the city that matches 39.

urbanCityOutlier = urbanRideCount[urbanRideCount==39].index[0]
print(f'{urbanCityOutlier} has the highest rider count')


# In[172]:


# Add urban fare box-and-whisker 
xLabels = ['Urban']
fig, ax = plt.subplots()
ax.boxplot(urbanFares, labels=xLabels)
ax.set_title('Ride Fare Data (2019)')
ax.set_ylabel('Fare($USD)')
ax.set_yticks(np.arange(0,51, step=5.0))
ax.grid()
plt.show()
print("Summary Statistics")
urbanFares.describe


# In[173]:


# Add suburban fare box-and-whisker 
xLabels = ['Suburban']
fig, ax = plt.subplots()
ax.boxplot(subFares, labels=xLabels)
ax.set_title('Ride Fare Data (2019)')
ax.set_ylabel('Fare($USD)')
ax.set_yticks(np.arange(0,51, step=5.0))
ax.grid()
plt.show()
print("Summary Statistics")
subFares.describe


# In[174]:


# Add rural fare box-and-whisker 
xLabels = ['Rural']
fig, ax = plt.subplots()
ax.boxplot(ruralFares, labels=xLabels)
ax.set_title('Ride Fare Data (2019)')
ax.set_ylabel('Fare($USD)')
ax.set_yticks(np.arange(0,51, step=5.0))
ax.grid()
plt.show()
print("Summary Statistics")
ruralFares.describe


# In[175]:


# Add all ride fare box-and-whisker plots to the same graph.
xLabels = ['Urban','Suburban','Rural']
rideFareData = [urbanFares, subFares,ruralFares]

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title('Ride Fare Data (2019)',fontsize=20)
ax.set_ylabel('Fare($USD)',fontsize=14)
ax.set_xlabel('City Types',fontsize=14)
ax.boxplot(rideFareData, labels=xLabels)
ax.set_yticks(np.arange(0,60, step=5.0))
ax.grid()
#saving figure
plt.savefig('Analysis/Fig3.png')
plt.show()


# In[176]:


# Create the box-and-whisker plot for the urban driver count data.
xLabels = ['Urban']

fig,ax = plt.subplots()
ax.boxplot(urbanDrivers, labels=xLabels)
ax.set_title('Driver Count Data (2019)')
ax.set_ylabel('Number of Drivers')
ax.set_yticks(np.arange(0,90,step=5.0))
ax.grid()
plt.show()
print("Summary Statistics")
urbanDrivers.describe()


# In[177]:


# Create the box-and-whisker plot for the rural driver count data.
xLabels = ['Rural']

fig,ax = plt.subplots()
ax.boxplot(ruralDrivers, labels=xLabels)
ax.set_title('Driver Count Data (2019)')
ax.set_ylabel('Number of Drivers')
ax.set_yticks(np.arange(0,90,step=5.0))
ax.grid()
plt.show()
print("Summary Statistics")
ruralDrivers.describe()


# In[178]:


# Create the box-and-whisker plot for the suburban driver count data.
xLabels = ['Suburban']

fig,ax = plt.subplots()
ax.boxplot(subDrivers, labels=xLabels)
ax.set_title('Driver Count Data (2019)')
ax.set_ylabel('Number of Drivers')
ax.set_yticks(np.arange(0,90,step=5.0))
ax.grid()
plt.show()
print("Summary Statistics")
subDrivers.describe()


# In[179]:


#Merging driver data into one whisker plot
xLabels = ['Urban','Suburban','Rural']
driverData = [urbanDrivers,subDrivers,ruralDrivers]

fig,ax = plt.subplots(figsize=(10, 6))
ax.set_title('Driver Data (2019)',fontsize=14)
ax.set_ylabel('Number of Drivers',fontsize=14)
ax.set_xlabel('City Types')
ax.set_yticks(np.arange(0,80,step=5))
ax.boxplot(driverData,labels=xLabels)
ax.grid()
#saving figure
plt.savefig('Analysis/Fig4.png')
plt.show()


# In[180]:


#Getting the sum of the Fares for each city type
sumFaresByType = pyberDataDf.groupby(['type']).sum()['fare']
sumFaresByType


# In[181]:


#Getting the total fare
totalFare  = pyberDataDf['fare'].sum()
totalFare


# In[182]:


#Calculating the percentage of fare for each city type
typePercents = sumFaresByType / totalFare * 100
typePercents


# In[183]:


#One line version of percentage calculation
oneLineTypePerc = (pyberDataDf.groupby(['type']).sum()['fare'] / pyberDataDf['fare'].sum()) * 100
oneLineTypePerc


# In[190]:


# Building the percentage of fares by city type pie chart
plt.subplots(figsize=(10,6))
plt.pie(typePercents,
        labels=['Rural','Suburban','Urban'],
        colors=['gold','lightskyblue','lightcoral'],
        explode=[0,0,0.1],
        autopct='%1.1f%%',
        shadow=True, startangle=150)
plt.title('% of Total Fares by City Type')

#changing default font size
mpl.rcParams['font.size'] = 14

#saving figure
plt.savefig('Analysis/Fig5.png')

plt.show()


# In[192]:


#Calculating the percentage of rides for each city type
ridePercents = (pyberDataDf.groupby(['type']).count()['ride_id'] / pyberDataDf['ride_id'].count()) * 100
ridePercents


# In[193]:


# Building the percentage of rides by city type pie chart
plt.subplots(figsize=(10,6))
plt.pie(ridePercents,
        labels=['Rural','Suburban','Urban'],
        colors=['gold','lightskyblue','lightcoral'],
        explode=[0,0,0.1],
        autopct='%1.1f%%',
        shadow=True, startangle=150)
plt.title('% of Total Rides by City Type')

#changing default font size
mpl.rcParams['font.size'] = 14
#saving figure
plt.savefig('Analysis/Fig6.png')

plt.show()


# In[194]:


#Calculating the percentage of drivers for each city type
driverPercents = (cityDf.groupby(['type']).sum()['driver_count'] / cityDf['driver_count'].sum()) * 100
driverPercents


# In[195]:



# Building the percentage of drivers by city type pie chart
plt.subplots(figsize=(10,6))
plt.pie(driverPercents,
        labels=['Rural','Suburban','Urban'],
        colors=['gold','lightskyblue','lightcoral'],
        explode=[0,0,0.1],
        autopct='%1.1f%%',
        shadow=True, startangle=165)
plt.title('% of Total Drivers by City Type')

#changing default font size
mpl.rcParams['font.size'] = 14
#saving figure
plt.savefig('Analysis/Fig7.png')

plt.show()


# In[ ]:




