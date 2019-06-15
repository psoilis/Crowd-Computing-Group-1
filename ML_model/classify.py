from classification import RandomForest, NaiveBayes, MaximumEntropy, XGBoost
from sklearn.model_selection import train_test_split
import pandas as pd

RANDOM_STATE = 123

df = pd.read_csv('data/features.csv')

X = df.loc[:, ~df.columns.isin(['Label', 'Tweet_ID'])].values

y = df['Label'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=RANDOM_STATE)

# test classifiers with confidence output tuple (confidence, judgment) confidence -> 0 (low confidence), 1 (high)
#                                                                      judgment -> 0 (not credible), 1 (credible)
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
