### Random forest Regression and Variable Importance 
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
