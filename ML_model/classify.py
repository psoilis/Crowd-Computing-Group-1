from classification import RandomForest, NaiveBayes, MaximumEntropy, XGBoost
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split


# test classifiers with confidence output -> -1 for uncertain 0 for (class 1) 1 for (class 2)
# TODO: change X, y to read them from features.csv
RANDOM_STATE = 123

X, y = make_classification(n_samples=500, n_features=25,
                           n_clusters_per_class=1, n_informative=15,
                           random_state=RANDOM_STATE)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

rf = RandomForest.RandomForest()
rf.train(x_train=X_train, y_train=y_train)
print(rf.predict_with_confidence(data=X_test, confidence=0.1))

xgb = XGBoost.XGBoost()
xgb.train(x_train=X_train, y_train=y_train)
print(xgb.predict_with_confidence(data=X_test, confidence=0.1))

nb = NaiveBayes.NaiveBayes()
nb.train(x_train=X_train, y_train=y_train)
print(nb.predict_with_confidence(data=X_test, confidence=0.1))

me = MaximumEntropy.MaximumEntropy()
me.train(x_train=X_train, y_train=y_train)
print(me.predict_with_confidence(data=X_test, confidence=0.1))
