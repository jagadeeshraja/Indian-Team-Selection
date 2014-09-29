import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.tools.plotting import parallel_coordinates
from sklearn.ensemble import RandomForestClassifier


batting = pd.read_csv("/home/jagadeesh/fuzzy/batting.csv")
batting['Age'] = (2014 - batting['Start'] ) + 16

##plot to show batsmen's minimum age so that we can reject the senior citizens from out test players list
plt.title("Histogram of Batsmen's minimum expected Age ")
batting['Age'].hist(bins= 50, figsize=(12,6))
plt.show()

## Removing players more than 70 years old (assuming debut age > 16)
batting1 = batting[batting['Start']>1960]

## Removing Irrelevent variables and creating new variables based on analysis
cols = [col for col in batting1.columns if col not in ['Start', 'End']]
batting2 = batting1[cols]
batting2['World'] = batting1['World'].fillna(0)
batting2['Not Out on Highest  Score'] = batting1['Not Out on Highest  Score'].fillna('Out')
du = pd.get_dummies(batting2['Not Out on Highest  Score'])
batting2['HighNotOut'] = du.iloc[:,0]
batting2['Endurance'] = batting2['Not Out']/ batting2['Innings']
batting2['Scorability'] = batting2['Runs']/ batting2['Innings']

cols = [col for col in batting2.columns if col not in [ 'Not Out on Highest  Score']]
batting3 = batting2[cols]

##Plotting no of matches played
plt.title("Histogram of No of Matches Played")
batting3['Matches'].hist(bins= 50, figsize=(12,6))
plt.show()

## Removing irrelevent data
India = batting3[batting3['Country']== 'India']
Indiadata = India.dropna()

World = batting3[batting3['Country']!= 'India']
Worlddata = World.dropna()

### Data Pruning
IndiaFinal = India[India['Innings'] > 30]
Fin = IndiaFinal[IndiaFinal['Runs'] > 1000]
Worldfinal = World[World['Innings'] > 40]
worldnew = Worldfinal[Worldfinal['Average'] > 40]
data = worldnew.iloc[:,3:]


## Scaling the data for better analysis
df_norm = data  / (data.max() - data.min())
df_norm['World'] = data['World']
plt.figure(figsize=(14,6))
plt.title("Rest of the world batting Data Visualization using Parallel Coordinates")
parallel_coordinates(df_norm, 'World')


plt.figure();
bp = df_norm.boxplot(by='World', figsize=(13,13))

worldnew.to_csv("worlddata.csv")

Fin.to_csv("Indiabattingdata.csv")

datax = data.drop('World', axis=1)
y = data['World']

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
plt.title("Variable Importance for Batsmen Selection")
plt.show()
