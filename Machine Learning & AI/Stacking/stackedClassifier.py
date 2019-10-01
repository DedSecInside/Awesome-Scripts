import numpy as np 
from sklearn import model_selection
from xgboost import XGBClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from mlxtend.classifier import StackingClassifier
from sklearn.ensemble import ExtraTreesClassifier

import warnings
warnings.filterwarnings("ignore")

dataset = np.loadtxt('../Dataset/comb.csv', delimiter=",")
# split data into X and y
X = dataset[:,0:np.array(dataset).shape[1] - 1]
y = dataset[:,np.array(dataset).shape[1] - 1]

clf1 = GradientBoostingClassifier()
clf2 = RandomForestClassifier(random_state=1)
clf4 = ExtraTreesClassifier()
xgb = XGBClassifier()
sclf = StackingClassifier(classifiers=[clf1, clf2, clf4], 
                          meta_classifier=xgb)

print('5-fold cross validation:\n')

for clf, label in zip([clf1, clf2, clf4, sclf], 
                      ['Gradient Boost', 
                       'Random Forest', 
                       'ExtraTrees Classifier',
                       'StackingClassifier']):
    scores = model_selection.cross_val_score(clf,X,y, cv=5, scoring='accuracy')
    print("Accuracy: %0.2f (+/- %0.2f) [%s]" % (scores.mean(), scores.std(), label))
                                                 