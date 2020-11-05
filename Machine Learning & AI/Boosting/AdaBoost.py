import numpy as np
from sklearn.ensemble import AdaBoostClassifier
import csv
import random

def main():
    """
    Main function.

    Args:
    """
	# prepare data
	trainingSet=[]
	testSet=[]
	accuracy = 0.0
	split = 0.20
	loadDataset('../Dataset/med.data', split, trainingSet, testSet)
	print('Train set: ' + repr(len(trainingSet)))
	print('Test set: ' + repr(len(testSet)))
	trainData = np.array(trainingSet)[:,0:np.array(trainingSet).shape[1] - 1]
	columns = trainData.shape[1] 
	X = np.array(trainData)
	y = np.array(trainingSet)[:,columns]
	clf = AdaBoostClassifier()
	clf.fit(X, y)
	testData = np.array(testSet)[:,0:np.array(trainingSet).shape[1] - 1]
	X_test = np.array(testData)
	y_test = np.array(testSet)[:,columns]
	accuracy = clf.score(X_test,y_test)
	accuracy *= 100
	print("Accuracy %:",accuracy)	




def loadDataset(filename, split, trainingSet=[] , testSet=[]):
    """
    Load a dataset.

    Args:
        filename: (str): write your description
        split: (str): write your description
        trainingSet: (todo): write your description
        testSet: (list): write your description
    """
	with open(filename, 'rt') as csvfile:
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
	

