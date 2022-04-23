#!/usr/bin/env python
# coding: utf-8

# In[24]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[25]:


#Importing dependencies
import matplotlib.pyplot as plt
import statistics


# In[26]:


# Setting the x-axis to a list of strings for each month.
x_axis = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

# Setting the y-axis to a list of floats as the total fare in US dollars accumulated for each month.
y_axis = [10.02, 23.24, 39.20, 35.42, 32.34, 27.04, 43.82, 10.56, 11.85, 27.90, 20.71, 20.09]


# In[27]:


#Getting standard deviavtion of y_axis values
stdev = statistics.stdev(y_axis)
stdev


# In[28]:


plt.errorbar(x_axis,y_axis,yerr=stdev,capsize=3)


# In[29]:


fig, ax = plt.subplots()
ax.errorbar(x_axis,y_axis, yerr=stdev, capsize=3)


# In[30]:


plt.bar(x_axis,y_axis,yerr=stdev, capsize=3)


# In[31]:


fig, ax = plt.subplots()
ax.bar(x_axis,y_axis, yerr=stdev, capsize=3)


# In[32]:


#importing numpy dependency as np
import numpy as np


# In[33]:


#creates a horizontal bar graph with the x_axis values
#incremented by 5.
plt.barh(x_axis,y_axis)
plt.xticks(np.arange(0,51, step=5.0))
#Inverts y_axis to have January at the top
plt.gca().invert_yaxis()


# In[34]:


np.arange(0,51, step=5.0)


# In[35]:


#Creates a horizontal bar graph using the OOP approach
fig, ax = plt.subplots()
ax.barh(x_axis,y_axis)
#x_axis values incremented by 5.
ax.set_xticks(np.arange(0,51, step=5.0))


# In[36]:


from matplotlib.ticker import MultipleLocator
#Icreases the siz of the plot figure
fig, ax = plt.subplots(figsize=(8,8))
#Creates bar graph with minor ticks
ax.barh(x_axis,y_axis)
ax.set_xticks(np.arange(0,51, step=5.0))
#Creating the minor ticks. Increment of 1.
ax.xaxis.set_minor_locator(MultipleLocator(1))
plt.show()


# In[ ]:




