# Hubway Data Challenge (work in progress)
An exploratory data analysis of the [Hubway dataset](http://hubwaydatachallenge.org/).

The Hubway dataset consists of 1,579,025 bicycle trips from its launch in 2011 to November 2013. Although the dataset consists of a variety of attributes, this analysis will focus on the following:

-	Start date and time
-	End date and time
-	Trip duration
-	Subscription type (registered or casual)
-	Zip code
-	Birth date
-	Gender

Note that many attributes have missing information, which will be explained later on. See the Python code in this repo for the steps taken to clean and format the data.

## Plotting the basics
Let's start with gender distribution. Some attributes, like gender, have information available only for registered trips.

![Figure1](https://github.com/faisale/hubway-data-challenge/blob/master/images/registered_trips_gender.png?raw=true)

<b>75.4%</b> of registered trips are made by males, and <b>24.6%</b> by females.

## Frequency by time and date

Let's take a look at the hourly distribution of the entire dataset:

![Figure2](https://github.com/faisale/hubway-data-challenge/blob/master/images/hourly_trip_dist.png?raw=true)

It's no surprise that most trips are made during office hours. However, what's interesting is that the number of trips at 8:00AM and 5:00PM peak. This suggests that many users use the bikes for their commute. Let's investigate further by plotting the trip frequency by days:

![Figure3](https://github.com/faisale/hubway-data-challenge/blob/master/images/day_trip_dist.png?raw=true)

It seems like there's a sharp decrease in activity on the weekends. What if we compare the hourly trip distribution by weekdays and weekends?

![Figure4](https://github.com/faisale/hubway-data-challenge/blob/master/images/weekday_trip_dist.png?raw=true)
![Figure5](https://github.com/faisale/hubway-data-challenge/blob/master/images/weekend_trip_dist.png?raw=true)

Indeed, it looks like our intuition is true! The 8:00AM and 5:00PM peaks are higher when isolating for weekdays. The hours in between don't see as much activity due to work. Additionally, the weekend distribution is quite different; users enjoy their rides in the middle of the day.

## Seasonality

Moving away from distributions, plotting a time series gives visual evidence of seasonality. What's interesting is that sometimes, data visualization will tell us something about the properties of the dataset that we weren't aware of. For example, the months of December - February are missing. This suggests that the program shuts down during the winter season.

![Figure6](https://github.com/faisale/hubway-data-challenge/blob/master/images/trips_month_year.png?raw=true)

Here, we can make a few observations:

- There is seasonality.
- Bike usage is generally increasing over the years.
- Activity during the summer months is increasing relative to its year's activity.

Categorizing activity by month over the years:

![Figure7](https://github.com/faisale/hubway-data-challenge/blob/master/images/trips_month.png?raw=true)

We can see that for the months of June, July and August, acitvity increases quite a bit, which explains the peak increase in the previous plot.

I should mention that the program started in July of 2011. However, it seems that there was no acitivity for March in 2013. There may have been a late return to the program that year.

## More to come

This analysis is a work in progress. There is a large section of the dataset I have yet touched and am working on analyzing. I will continuously update this repo along the way.
