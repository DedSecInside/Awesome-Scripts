import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from math import sqrt
from sklearn.model_selection import train_test_split

def main():
    """
    Main function.

    Args:
    """

    df = pd.read_csv('father_son.csv',error_bad_lines=False, delimiter=',')
    X = df['Father'].values[:,np.newaxis]
    y = df['Son'].values
    print("Loading ...")
    #Find the mean
    x_mean = mean(X)
    y_mean = mean(y)
    #Subtract mean from the points
    sub_X = sub(X,x_mean) 
    sub_y = sub(y,y_mean)
    #Multiply x and y
    mult_Xy = mul(sub_X,sub_y)
    meansq = meanSquared(sub_X)

    sumMul = sumXY(mult_Xy)
    sumMeansq =  sumXY(meansq)

    B1 = sumMul/sumMeansq
    B0 = y_mean - B1 * x_mean

    predicted = predict(X,B1,B0)

    print(sqrt(RMSE(predicted,y)/5))
    plt.scatter(X,y)
    plt.scatter(predicted,predicted)
    plt.xlabel((sqrt(RMSE(predicted,y)/5)))
    plt.ylabel('predicted')

    plt.show()


def mean(n):
    """
    Calculate mean of the distribution.

    Args:
        n: (array): write your description
    """
    s = 0
    length = len(n)
    for j in range(0,length):
    	s = s+n[j]
    mean = s/length	
    return mean

def sub(x,mean):
    """
    Returns the mean of x.

    Args:
        x: (int): write your description
        mean: (int): write your description
    """
    arr = []
    length = len(x) 
    for j in range(0,length):
        arr.append(x[j] - mean)   
    return arr

def mul(x,y):
    """
    Mul ( x y - > y

    Args:
        x: (array): write your description
        y: (array): write your description
    """
    mult = []
    length = len(x)
    for j in range(0,length):
        mult.append(x[j] * y[j])
    return mult     

def meanSquared(x):
    """
    Calculate mean of x.

    Args:
        x: (array): write your description
    """
    meansq = []
    length = len(x)
    for j in range(0,length):
        meansq.append(x[j][0] *x[j][0])
    return meansq   

def sumXY(x):
    """
    Returns the sum of x.

    Args:
        x: (todo): write your description
    """
    sumRes = 0
    length = len(x)
    for j in range(0,length):
        sumRes = sumRes + x[j]
    return sumRes
  
def predict(x,B1,B0):
    """
    Predict the values of x1 x1.

    Args:
        x: (array): write your description
        B1: (array): write your description
        B0: (array): write your description
    """
    pred = []
    length = len(x)
    for j in range(0,length):
        pred.append(B0+B1*x[j])
    return pred    

def RMSE(predicted,y):
    """
    Calculates error.

    Args:
        predicted: (todo): write your description
        y: (array): write your description
    """
    rmse = 0
    error = []
    errorsq = []
    length = len(y)
    for i in range(0,length):
        error.append(predicted[i] - y[i])
    for j in range(0,length):
        errorsq.append(error[j][0] * error[j][0])
    for k in range (0,length):
        rmse = rmse + errorsq[k]
    return rmse


main()

