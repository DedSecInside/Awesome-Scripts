from sklearn.feature_selection import RFECV
from xgboost import XGBClassifier
from numpy import loadtxt
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

dataset = loadtxt('../Dataset/heart.data', delimiter=",")
# split data into X and y
X = dataset[:,0:np.array(dataset).shape[1] - 1]
Y = dataset[:,np.array(dataset).shape[1] - 1]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.23, random_state=22) 
#use linear regression as the model
xg = XGBClassifier()
#rank all features, i.e continue the elimination until the last one
rfe = RFECV(xg, cv=5, step=1)
rfe.fit(X_train,y_train)
y_important_pred = rfe.predict(X_test)

print("Features sorted by their rank:")
print(sorted(zip(map(lambda x:x, rfe.ranking_))))
print(sorted(zip(map(lambda x:x, rfe.support_))))
print(accuracy_score(y_test, y_important_pred.round()) * 100)