import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

X, y = load_iris(return_X_y=True)
clf = RandomForestClassifier(n_estimators=10)
clf.fit(X, y)

joblib.dump(clf, "model.pkl")