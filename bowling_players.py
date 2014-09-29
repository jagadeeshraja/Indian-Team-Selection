
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.tools.plotting import parallel_coordinates
from sklearn.ensemble import RandomForestClassifier

##getting the data for bowling
bowling = pd.read_csv("/home/jagadeesh/fuzzy/bowling.csv")
print bowling.shape


## Visulising the age of the players (assuming the players debut age > 16)
bowling['Age'] = (2014 - bowling['Span'] ) + 16
plt.title("Histogram of Bowler's minimum expected Age ")
bowling['Age'].hist(bins= 50, figsize=(12,6))

## Removing players more than 70 yeras old from our consideration
bowling1 = bowling[bowling['Span']>1960]

## Remove irrelevant variables and add derived variables for analysis
cols = [col for col in bowling1.columns if col not in ['Span', 'end']]
bowling2 = bowling1[cols]
bowling2['world'] = bowling2['world'].fillna(0)
bowlindata = bowling2.dropna()
bowlindata['BestB Inning'] = bowlindata['Best B Inning1']/ bowlindata['Best B Inning2']
bowlindata['BestBInning'] = bowlindata['Best B Match1']/ bowlindata['Best B Match2']
bowlindata['Wickt/Inning'] = bowlindata['Wickets']/ bowlindata['Innings']
bowlindata['ball/inning'] = bowlindata['Balls']/ bowlindata['Innings']
cols = [col for col in bowlindata.columns if col not in ['Best B Inning1', 'Best B Inning2', 'Best B Match1','Best B Match2']]
bowling3 = bowlindata[cols]

# Visualising statistics for no of matches played
plt.title("Histogram of No of Matches Played")
bowling3['Matches'].hist(bins= 50, figsize=(12,6))


## Data Pruning
India = bowling3[bowling3['Country']== 'India']
World = bowling3[bowling3['Country']!= 'India']

Indiadata = IndiaFinal[IndiaFinal['Wickets'] > 50]
Worldfinal = World[World['Innings'] > 30]
worldnew = Worldfinal[Worldfinal['Wickets'] > 50]
data = worldnew.iloc[:,3:]

### Scaling the data for better visualization
df_norm = data  / (data.max() - data.min())
df_norm['world'] = data['world']
plt.figure(figsize=(16,6))
plt.title("Rest of the world Bowling Data Visualization using Parallel Coordinates")
parallel_coordinates(df_norm, 'world')


## writing the output files
worldnew.to_csv("worlddatabowling.csv")
Indiadata.to_csv("indiadatabowling.csv")
