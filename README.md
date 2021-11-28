# PyBer_Analysis
## Overview & Purpose of Analysis
PyPer wants to know more about their ride sharing data for each city type: ```Urban```, ```Rural```, ```Suburban```.
Specifically, two datasets ([City Data](https://github.com/StickySitch/PyBer_Analysis/blob/main/Resources/city_data.csv) & [Ride Data](https://github.com/StickySitch/PyBer_Analysis/blob/main/Resources/ride_data.csv)) 
have been merged to calculate and present each city types data:
#### Calculated & Presented Data for Each City Type:
- Total Rides
- Total Drivers
- Total Fares
- Average Fare Per Ride
- Average Fare Per Driver
##### Presentation - ```Line Chart```:
- Total Fare by City Type

## Resources
- ```Data Sources:``` [city_data.csv](https://github.com/StickySitch/PyBer_Analysis/blob/main/Resources/city_data.csv) **|** [ride_data.csv](https://github.com/StickySitch/PyBer_Analysis/blob/main/Resources/ride_data.csv)
- ```Software:``` [Python 3.8.8](https://www.python.org/downloads/release/python-388/) **|** [Jupyter Notebook 6.3.0](https://jupyter.org/)
- ```Libraries:``` [Matplotlib 3.3.4](https://matplotlib.org/3.3.4/index.html) **|** [Pandas 1.2.4](https://pandas.pydata.org/pandas-docs/stable/whatsnew/v1.2.4.html)
- ```Source Code:``` [PyBer_Challenge.ipynb](https://github.com/StickySitch/PyBer_Analysis/blob/main/PyBer_Challenge.ipynb)
## Results
### PyBer Total Summary DataFrame
To begin our analysis, we will need take a look at our ```pyber_summary_df``` dataframe below.

![PyBerSummaryDf](https://github.com/StickySitch/PyBer_Analysis/blob/main/Analysis/PyBerSummaryDf.png)

As you can see in the image, the data presented is sorted by ```city type```. Let's break this data down a little bit
to compare the three city types.

**```Data From: January 1st, To: April 30th```**
- Total Rides:
  - Rural - ```125```
  - Suburban - ```625```
  - Urban - ```1,625```
  
Lets talk about the ```Total Rides``` breakdown. Right off the bat, we can see a wide ride count range; With rural cities
being the lowest of the counts at ```125 rides``` and urban cities having the highest count of ```1,625 rides```. We will
talking about these differences in a minute once we have gone over the ```Total Drivers``` and ```Total Fares``` data.              

- Total Drivers:
  - Rural - ```78```
  - Suburban - ```490```
  - Urban - ```2,405```

Now the ```Total Drivers``` data. Just like above, we have another big difference in values. Once again, rural cities
have the lowest ```Total Driver``` count of ```78 drivers```. We have suburban cities sitting at ```490 drivers``` and our
highest driver count of ```2,405 drivers``` coming from urban cities.

- Total Fares:
  - Rural - ```$4,327.93```
  - Suburban - ```$19,356.33```
  - Urban - ```$39,854.38```

Money time! As you would suspect the money adds up! Due to rural cities having the lowest ```Total Drivers``` and ```Total Riders```,
their ```Total Fare``` count is also the lowest: ```$4,327.93```. Suburban cities coming in second again with a ```Total Fare```
of ```$19,356.33```. Last but **definitely** not least, urban cities ```Total Fare``` count: ```$39,854.38```

Alright, before we continue with the breakdown, I want to talk about the differences in the data from each city type. When it
comes to the data, there is one undeniable factor; Population. The data presented above is a perfect example of supply and demand.
In general, rural cities are known for lower populations, meaning fewer people are looking for rides as well as fewer drivers are looking for riders!
This one factor alone dictates the majority of the data above.

Urban cities are much higher in population. Another factor to think about here is life style. Let's look at urban cities for example.
Unlike rural cities, urban cities are packed tight. Sometimes so tight, owning a car isn't even recommended. With this in mind, it's
safe to assume ride sharing and public transportation are used much more.
- Average Fare Per Ride:
  - Rural - ```$34.62```
  - Suburban - ```$30.97```
  - Urban - ```$24.53```

Back to the data! Above you can see our ```Average Fare Per Ride Data```. Now the data displays the following: **Rural** - ```$34.62``` | **Suburban** - ```$30.97```
| **Urban** - ```$24.53```.

Now interestingly, rural cities has the highest ```Average Fare Per Ride``` and urban cities has the lowest. This can be
directly correlated to the driver count and rider count. Due to there not being enough drivers to service the area, prices are higher.
Distance is also a factor. Like I mentioned earlier, urban cities are packed tight so it is likely that less distance will
be traveled. Rural cities will have more distance to cover between place to place, therefor adding to the ```Average Fare Per Ride```.
- Average Fare Per Driver:
  - Rural - ```$55.49```
  - Suburban - ```$39.50```
  - Urban - ```$16.57```

Lastly, we can see the ```Average Fare Per Driver``` data for each city type listed above. First, lets take a look at the average fare
for rural city drivers: ```$55.49```. Compared to rural cities, Suburban(```$39.50```) & Urban (```$16.57```) drivers average
fares are significantly lower. If you look above at our ```Total Drivers``` & ```Total Rides``` datasets and compare them to the ```Average Fare Per Driver:``` 
dataset, you can see that as the driver count rises, the fare lowers. Again, supply and demand. For example, Urban cities have a
```Total Rides``` count of ```1,625 rides``` but also had a ```Total Drivers``` count of ```2,405```. As you can see, the drivers
outweigh the riders! One last time just to hit it home; life style based on city type will always have factors here. I.E. distance,
necessity for a car & population.

### PyBer Total Fare by City Type Multi-line Chart

Our last set of data to look at is in the form of a multi-line chart. Below you can see a multi-line chart representing the ```Total Fare by City Type``` data.
This data is over a 4 month period starting January 1st going up until April 30th.

![Multiline Chart](https://github.com/StickySitch/PyBer_Analysis/blob/main/Analysis/PyBer_fare_summary.png)

- ```Rural Cities```
  - Fare range: $0 - $500
- ```Suburban Cities```
  - Fare range: $600 - $1,500
- ```Urban Cities```
  - Fare range: $1,600 - $2,500

You can see decent amount of fluctuation for each of these city types. The cause for this fluctuation is simple, our good only friend
supply and demand. During the down times, rider counts were likely lower causing the decrease in revenue.

## Summary
After seeing all of this data, it is clear that there is room for improvement for PyBer. I've gone ahead and listed my 3 recommendations
for improvement below:

### 1. Increase Total Fare for Rural Cities by Increasing Drivers
Rural cities are the least active ride sharing cities out of the bunch. In order to increase the money that is flowing, we need two things:
More drivers and more riders! The biggest problem with rural cities is their population density. With there not being enough drivers to service 
the area, riders aren't incentivized to ride share due to their higher rates. Since rural areas often have neighboring Urban cities
my suggestion is to incentivize the drivers from these larger neighboring cities to drive a little further out to service that area.
By doing this, riders will automatically increase due to the service being usable without being charged an arm and a leg.

### 2. Decrease Total Driver In Urban Cities
This suggestion couples nicely with the first. We need decrease the amount of drivers in Urban cities in order to make ride sharing a 
sustainable and reliable income for each drive. To do this, as I suggested in the first proposal, outsource the Urban city drivers 
to the rural areas! Two birds, one stone! By doing this, we not only increase revenue from rural areas, our revenue from Urban cities 
shouldn't decrease due to our abundance of drivers.

### 3. Increase The Number of Suburban Drivers
My final recommendation is to increase the number of Suburban drivers. To increase the driver count, the demand needs to be higher 
as well. Now, for me this is a tricky one. How do you get those that don't need ride share, to want ride share? My suggestion is to
run promotions on weekends and Holidays for both the drivers and riders. With these weekend promotions, drivers will be paid a little more, while the weekend
and Holiday riders get a much needed service. Those who have indulge in alcohol can now get home safe!