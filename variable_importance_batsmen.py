
## Fitting a random forest regression to create importance score for identifying the best batsmen

datax = data.drop('World', axis=1)
y = data['World']
features = datax.columns
clf = RandomForestClassifier(n_estimators=500, compute_importances=True)
clf.fit(datax, y)
importances = clf.feature_importances_
sorted_idx = np.argsort(importances)

## Visualizing the importance scores
padding = np.arange(len(features)) + 0.5
plt.figure(figsize=(12,6))
plt.barh(padding, importances[sorted_idx], align='center')
plt.yticks(padding, features[sorted_idx])
plt.xlabel("Relative Importance")
plt.title("Variable Importance for Batsmen Selection")
plt.show()
