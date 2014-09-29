
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.tools.plotting import parallel_coordinates
from sklearn.ensemble import RandomForestClassifier


bowling = pd.read_csv("/home/jagadeesh/fuzzy/bowling.csv")
print bowling.shape

bowling['Age'] = (2014 - bowling['Span'] ) + 16
plt.title("Histogram of Bowler's minimum expected Age ")
bowling['Age'].hist(bins= 50, figsize=(12,6))

bowling1 = bowling[bowling['Span']>1960]
print bowling1.shape
cols = [col for col in bowling1.columns if col not in ['Span', 'end']]
bowling2 = bowling1[cols]
bowling2['world'] = bowling2['world'].fillna(0)
print bowling2.columns
bowlindata = bowling2.dropna()
bowlindata['BestB Inning'] = bowlindata['Best B Inning1']/ bowlindata['Best B Inning2']
bowlindata['BestBInning'] = bowlindata['Best B Match1']/ bowlindata['Best B Match2']
bowlindata['Wickt/Inning'] = bowlindata['Wickets']/ bowlindata['Innings']
bowlindata['ball/inning'] = bowlindata['Balls']/ bowlindata['Innings']

cols = [col for col in bowlindata.columns if col not in ['Best B Inning1', 'Best B Inning2', 'Best B Match1','Best B Match2']]
bowling3 = bowlindata[cols]
print bowling3.shape
bowling3.head()

bowling3[bowling3['world']==1]

bowling3.head()

plt.title("Histogram of No of Matches Played")
bowling3['Matches'].hist(bins= 50, figsize=(12,6))

bowling3['Country'].unique()

India = bowling3[bowling3['Country']== 'India']
World = bowling3[bowling3['Country']!= 'India']

Indiadata = IndiaFinal[IndiaFinal['Wickets'] > 50]
Worldfinal = World[World['Innings'] > 30]
worldnew = Worldfinal[Worldfinal['Wickets'] > 50]
data = worldnew.iloc[:,3:]


df_norm = data  / (data.max() - data.min())
df_norm['world'] = data['world']
plt.figure(figsize=(16,6))
plt.title("Rest of the world Bowling Data Visualization using Parallel Coordinates")
parallel_coordinates(df_norm, 'world')



worldnew.to_csv("worlddatabowling.csv")
Indiadata.to_csv("indiadatabowling.csv")

datax = data.drop('world', axis=1)
y = data['world']
features = datax.columns
clf = RandomForestClassifier(n_estimators=500, compute_importances=True)
clf.fit(datax, y)
importances = clf.feature_importances_
sorted_idx = np.argsort(importances)
padding = np.arange(len(features)) + 0.5
plt.figure(figsize=(12,6))
plt.barh(padding, importances[sorted_idx], align='center')
plt.yticks(padding, features[sorted_idx])
plt.xlabel("Relative Importance")
plt.title("Variable Importance for bowler selection")
plt.show()
