### Fiiting a Random forest Regression and creating Variable Importance scores
datax = data.drop('world', axis=1)
y = data['world']
features = datax.columns
clf = RandomForestClassifier(n_estimators=500, compute_importances=True)
clf.fit(datax, y)
importances = clf.feature_importances_
sorted_idx = np.argsort(importances)

## Plotting the importance of each variables
padding = np.arange(len(features)) + 0.5
plt.figure(figsize=(12,6))
plt.barh(padding, importances[sorted_idx], align='center')
plt.yticks(padding, features[sorted_idx])
plt.xlabel("Relative Importance")
plt.title("Variable Importance for bowler selection")
plt.show()

## The variables are correlated here hence the scores are unreliable for correlated variables
