#!/usr/bin/env python
# coding: utf-8

# In[31]:


get_ipython().run_line_magic('matplotlib', 'inline')
#Importing dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Reading PyBer CSV file
pyberDf = pd.read_csv('Resources/PyBer_ride_data.csv')
pyberDf


# In[32]:


pyberDF.plot(x='Month',y='Avg. Fare ($USD)')
plt.show()


# In[33]:


#Setting xAxis and tick locations
xAxis = np.arange(len(pyberDf))
tickLocations = [value for value in xAxis]
#Plotting the Data
pyberDf.plot(x='Month',y='Avg. Fare ($USD)')
plt.xticks(tickLocations, pyberDf['Month'])


# In[54]:


x = 'Month'
y = 'Avg. Fare ($USD)'
import statistics
stdev = statistics.stdev(pyberDf['Avg. Fare ($USD)'])
#Creating a bar chart
pyberDf.plot.bar(x=x,y=y,label='Avg. Fare ($USD)',color='xkcd:sky blue',rot=0,yerr=stdev,capsize=3,yticks = np.arange(0,60, step=5.0))


# In[ ]:




