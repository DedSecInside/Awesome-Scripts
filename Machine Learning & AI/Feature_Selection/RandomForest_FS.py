import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score
from numpy import loadtxt
import csv
import random
from sklearn.svm import LinearSVC



def main():
    """
    Main function.

    Args:
    """

	trainingSet=[]
	testSet=[]
	accuracy = 0.0
	split = 0.25
	loadDataset('../Dataset/heart.data', split, trainingSet, testSet)
	# generate predictions
	predictions=[]
	trainData = np.array(trainingSet)[:,0:np.array(trainingSet).shape[1] - 1]
	columns = trainData.shape[1] 
	X_train = np.array(trainData).astype(np.float)
	y_train = np.array(trainingSet)[:,columns].astype(np.float)
	clf = RandomForestClassifier(n_estimators=100)
	clf.fit(X_train, y_train)
	testData = np.array(testSet)[:,0:np.array(trainingSet).shape[1] - 1]
	X_test = np.array(testData).astype(np.float)
	y_test = np.array(testSet)[:,columns].astype(np.float)
	y_pred = clf.predict(X_test)
	print("Before Feature Selection",accuracy_score(y_test, y_pred))

	# Create a random forest classifier
	clf = LinearSVC(random_state=0, tol=1e-5)
	# Train the classifier
	clf.fit(X_train, y_train)

	# Print the gini importance of each feature

	# Create a selector object that will use the random forest classifier to identify
	sfm = SelectFromModel(clf, threshold=0.03)
	# Train the selector
	sfm.fit(X_train, y_train)


	# Transform the data to create a new dataset containing only the most important features
	# Note: We have to apply the transform to both the training X and test X data.
	X_important_train = sfm.transform(X_train)
	X_important_test = sfm.transform(X_test)

	# Create a new random forest classifier for the most important features
	clf_important = RandomForestClassifier(n_estimators=200)

	# Train the new classifier on the new dataset containing the most important features
	clf_important.fit(X_important_train, y_train)

	# Apply The Full Featured Classifier To The Test Data

	# View The Accuracy Of Our Full Feature Model

	# Apply The Full Featured Classifier To The Test Data
	y_important_pred = clf_important.predict(X_important_test)

	# View The Accuracy Of Our Limited Feature  Model
	print("After Feature Selection",accuracy_score(y_test, y_important_pred))

def loadDataset(filename, split, trainingSet=[] , testSet=[]):
    """
    Load a dataset.

    Args:
        filename: (str): write your description
        split: (str): write your description
        trainingSet: (todo): write your description
        testSet: (list): write your description
    """
	with open(filename, 'r') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)):
	        for y in range(np.array(dataset).shape[1]):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            testSet.append(dataset[x])
	        else:
	            trainingSet.append(dataset[x])

main()	            