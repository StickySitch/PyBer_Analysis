#!/usr/bin/env python
# coding: utf-8

# # Pyber Challenge

# ### 4.3 Loading and Reading CSV files

# In[398]:


# Add Matplotlib inline magic command
get_ipython().run_line_magic('matplotlib', 'inline')
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd

# File to Load (Remember to change these)
city_data_to_load = "Resources/city_data.csv"
ride_data_to_load = "Resources/ride_data.csv"

# Read the City and Ride Data
city_data_df = pd.read_csv(city_data_to_load)
ride_data_df = pd.read_csv(ride_data_to_load)


# ### Merge the DataFrames

# In[399]:


# Combine the data into a single dataset
pyber_data_df = pd.merge(ride_data_df, city_data_df, how="left", on=["city", "city"])

# Display the data table for preview
pyber_data_df


# ## Deliverable 1: Get a Summary DataFrame 

# In[400]:


#  1. Get the total rides for each city type
rideTotalByCityType = pyber_data_df.groupby(['type']).count()['ride_id']
rideTotalByCityType


# In[401]:


# 2. Get the total drivers for each city type
driverTotalByCityType = city_data_df.groupby(['type']).sum()['driver_count']
driverTotalByCityType


# In[402]:


#  3. Get the total amount of fares for each city type
fareTotalByCityType = pyber_data_df.groupby(['type']).sum()['fare']
fareTotalByCityType


# In[403]:


#  4. Get the average fare per ride for each city type. 
rideAvgFare = fareTotalByCityType / rideTotalByCityType
rideAvgFare


# In[404]:


# 5. Get the average fare per driver for each city type. 
driverAvgFare = fareTotalByCityType / driverTotalByCityType
driverAvgFare


# In[405]:


#  6. Create a PyBer summary DataFrame. 
pyber_summary_df = pd.DataFrame({
    'Total Rides': rideTotalByCityType,
    'Total Drivers': driverTotalByCityType,
    'Total Fares': fareTotalByCityType,
    'Average Fare Per Ride': rideAvgFare,
    'Average Fare Per Driver': driverAvgFare
})

pyber_summary_df


# In[406]:


#  7. Cleaning up the DataFrame. Delete the index name
pyber_summary_df.index.name = None
pyber_summary_df


# In[407]:


#  8. Format the columns.
#Adding dollar ($) signs to monetary columns and limiting to 2 decimal places
pyber_summary_df['Total Fares'] = pyber_summary_df['Total Fares'].apply('${:.2f}'.format)
pyber_summary_df['Average Fare Per Ride'] = pyber_summary_df['Average Fare Per Ride'].apply('${:.2f}'.format)
pyber_summary_df['Average Fare Per Driver'] = pyber_summary_df['Average Fare Per Driver'].apply('${:.2f}'.format)
#Adding commas to 4+ digit numbers
pyber_summary_df['Total Rides'] = pyber_summary_df['Total Rides'].apply('{:,}'.format)
pyber_summary_df['Total Drivers'] = pyber_summary_df['Total Drivers'].apply('{:,}'.format)
pyber_summary_df


# ## Deliverable 2.  Create a multiple line plot that shows the total weekly of the fares for each type of city.

# In[408]:


# 1. Read the merged DataFrame
pyber_data_df


# In[409]:


# 2. Using groupby() to create a new DataFrame showing the sum of the fares 
#  for each date where the indices are the city type and date.
lineChartDf = pyber_data_df.groupby(['type','date']).sum()['fare']
lineChartDf


# In[410]:


# 3. Reset the index on the DataFrame you created in #1. This is needed to use the 'pivot()' function.
lineChartDf = lineChartDf.reset_index()


# In[411]:


# 4. Create a pivot table with the 'date' as the index, the columns ='type', and values='fare' 
# to get the total fares for each type of city by the date. 
fareByDateDf = lineChartDf.pivot(index='date', columns='type', values='fare')
fareByDateDf


# In[412]:


# 5. Create a new DataFrame from the pivot table DataFrame using loc on the given dates, '2019-01-01':'2019-04-29'.
startDate = '2019-01-01'
endDate = '2019-04-29'

toAprilDf = fareByDateDf.loc['2019-01-01':'2019-04-29']
toAprilDf


# In[413]:


# 6. Set the "date" index to datetime datatype. This is necessary to use the resample() method in Step 8.
toAprilDf.index = pd.to_datetime(toAprilDf.index)


# In[414]:


# 7. Check that the datatype for the index is datetime using df.info()
toAprilDf.info()


# In[415]:


# 8. Create a new DataFrame using the "resample()" function by week 'W' and get the sum of the fares for each week.
weeklyFareDf = toAprilDf.resample('W').sum()
weeklyFareDf


# In[416]:


# 8. Using the object-oriented interface method, plot the resample DataFrame using the df.plot() function.
# Import the style from Matplotlib.
from matplotlib import style
style.use('fivethirtyeight')

weeklyFareDf.plot(figsize=(20,10),
                  title="PyBer Total Fare by City Type",
                  ylabel='Fare ($USD)',
                  xlabel='Date')

#Getting current y ticker values
currentValues = plt.gca().get_yticks()
#Chaning the y ticker values to be formatted with dollar ($) signs and thousands separators
plt.gca().set_yticklabels(['${:,.0f}'.format(x) for x in currentValues])

#moving legend(key) to upper right corner
plt.legend(loc='upper right')

#Saving line chart as png
plt.savefig('Analysis/PyBer_fare_summary.png')

#displaying the line chart
plt.show()


# In[416]:




