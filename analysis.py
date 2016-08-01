import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# Analysis for the Hubway data challenge. Time period is from
# the Hubway launch in Jul 28, 2011 - Nov 30, 2013.

stations_df = pd.read_csv('hubway_stations.csv', header=0)
trips_df = pd.read_csv('hubway_trips.csv', header=0)



trips_df['gender'].value_counts().plot(kind='bar')
plt.xticks(rotation=0)
plt.show()

trips_df['age'].hist(bins=len(trips_df['age'].unique()))
plt.show()

#plt.xlabel('Gender')
#plt.ylabel('Count')
#plt.title('Gender Distribution')

trips_df['F_start_date'] = pd.to_datetime(trips_df['start_date'], format='%m/%d/%Y %H:%M:%S')

trips_df['age'] = pd.DatetimeIndex(trips_df['F_start_date']).year - trips_df['birth_date']

#plt.show()

test = trips_df['duration'].value_counts()

hours = pd.Series(pd.DatetimeIndex(trips_df['F_start_date']).hour)

trips_df['Day'] = pd.DatetimeIndex(trips_df['F_start_date']).weekday

monthyear = 100*trips_df['F_start_date'].dt.year + trips_df['F_start_date'].dt.month
monthyear.value_counts()

weekdayhours = trips_df['F_start_date'][trips_df['F_start_date'].dt.dayofweek < 5].dt.hour

weekendhours = trips_df['F_start_date'][trips_df['F_start_date'].dt.dayofweek >= 5].dt.hour
