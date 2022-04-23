#!/usr/bin/env python
# coding: utf-8

# In[91]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[92]:


#Import dependencies
import matplotlib.pyplot as plt


# In[93]:


# Set the x-axis to a list of strings for each month.
x_axis = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

# Set the y-axis to a list of floats as the total fare in US dollars accumulated for each month.
y_axis = [10.02, 23.24, 39.20, 35.42, 32.34, 27.04, 43.82, 10.56, 11.85, 27.90, 20.71, 20.09]

plt.plot(x_axis,y_axis)


# In[94]:


#create plot with ax.plt()
fig, ax = plt.subplots()
ax.plot(x_axis,y_axis)


# In[95]:


#Create the plot with ax.plt() **ANOTHER OPTION**
fig = plt.figure()
ax = fig.add_subplot()
ax.plot(x_axis,y_axis)


# In[96]:


# Create the plot with ax.plt()
ax = plt.axes()
ax.plot(x_axis, y_axis)


# In[97]:


# Create the plot and add a label for the legend.
plt.plot(x_axis, y_axis, marker="*", color="green", linewidth=2, label='Boston')
# Create labels for the x and y axes.
plt.xlabel("Date")
plt.ylabel("Fare($)")
# Set the y limit between 0 and 45.
plt.ylim(0, 45)
# Create a title.
plt.title("PyBer Fare by Month")
# Add the legend.
plt.legend()
plt.grid()


# In[98]:


plt.bar(x_axis,y_axis)


# In[99]:


# Create the plot.
plt.bar(x_axis, y_axis, color="green", label='Boston')
# Create labels for the x and y axes.
plt.xlabel("Date")
plt.ylabel("Fare($)")
# Create a title.
plt.title("PyBer Fare by Month")
# Add the legend.
plt.legend()


# In[100]:


plt.barh(x_axis,y_axis, color='magenta', label='Boston')
plt.title('PyBer Fare by Month')
plt.xlabel('Fare ($)')
plt.ylabel('Date')
plt.legend()
plt.gca().invert_yaxis()


# In[101]:


fig, ax = plt.subplots()
ax.bar(x_axis,y_axis)


# In[102]:


fig, ax = plt.subplots()
ax.barh(x_axis,y_axis, color='cyan',label='Chicago')
ax.set_title('PyBer Fare by Month')
ax.set_xlabel('Fare ($)')
ax.set_ylabel('Date')
ax.invert_yaxis()
ax.legend()


# In[103]:


# Set the x-axis to a list of strings for each month.
x_axis = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

# Set the y-axis to a list of floats as the total fare in US dollars accumulated for each month.
y_axis = [10.02, 23.24, 39.20, 35.42, 32.34, 27.04, 43.82, 10.56, 11.85, 27.90, 20.71, 20.09]


# In[104]:


#Creating scatter plot using .plot()
plt.plot(y_axis, x_axis, 'o',color='red',label='Chicago')
plt.xlabel('Fare ($)')
plt.ylabel('Date')
plt.gca().invert_yaxis()
plt.legend()


# In[105]:


plt.scatter(x_axis,y_axis)


# In[106]:


#Creating a Bubble Chart
plt.scatter(x_axis,y_axis, s=y_axis)


# In[107]:


#resizing bubbles with python for loop
yAxisLarger = []
for data in y_axis:
    yAxisLarger.append(data*3)
plt.scatter(x_axis, y_axis, s=yAxisLarger)


# In[108]:


#resizing bubbles with list comprehension
plt.scatter(x_axis,y_axis, s=[i*3 for i in y_axis])


# In[109]:


#Creating Scatter Plot using OOP approach
fig, ax = plt.subplots()
ax.scatter(x_axis,y_axis)


# In[110]:


#Creating Bubble Chart using OOP approach
fig, ax = plt.subplots()
ax.scatter(y_axis,x_axis, s=[i*5 for i in y_axis],color='xkcd:sky blue',edgecolors='black',alpha=0.80,linewidths=2,label='Boston')
ax.set_title('PyBer Fare By Month')
ax.set_xlabel('Fare ($)')
ax.set_ylabel('Date')
ax.set_xlim(0,45)
ax.invert_yaxis()
ax.legend()


# In[111]:


plt.pie(y_axis, labels=x_axis)


# In[112]:


plt.subplots(figsize=(8,8))
explodeValues = (0, 0, 0, 0, 0, 0, 0.2, 0, 0, 0, 0, 0)

plt.pie(y_axis, explode=explodeValues, autopct='%1.1f%%')


# In[113]:


#Assigning specific colors to pie slices
colors = ["slateblue", "magenta", "lightblue", "green", "yellowgreen", "greenyellow", "yellow", "orange", "gold", "indianred", "tomato", "mistyrose"]
explodeValues = (0, 0, 0, 0, 0, 0, 0.2, 0, 0, 0, 0, 0)
plt.subplots(figsize=(8,8))
plt.pie(y_axis,
       explode=explodeValues,
       colors=colors,
        labels=x_axis,
       autopct='%.1f%%')
plt.show()


# In[134]:


#Creating pie chart using OOP approach
explodeValues = (0, 0, 0.2, 0, 0, 0, 0.2, 0, 0, 0, 0, 0)
fig, ax = plt.subplots(figsize=(8,8))
ax.pie(y_axis, labels=x_axis, colors=colors, explode=explodeValues, autopct='%.1f%%',shadow=True,startangle=95,counterclock=False)
plt.show()


# In[ ]:




