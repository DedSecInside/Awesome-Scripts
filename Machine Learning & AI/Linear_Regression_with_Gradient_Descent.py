'''
Y is the dependant variable and X is the independant variable
We are going to fit a line
        Y = a0 + a1*x
using Gradient Descent minimizing the SSE.
This code will work for any variable with single attribute, i.e.
it is Linear Regression in 1 variable.
'''
import random
import matplotlib.pyplot as plt
import numpy as np

#Sum of Squares Error
def sse(n,a0,a1,x,y):
    s=0
    mean=np.mean(y)
    for i in range(n):
        s+=(a0+a1*x[i]-mean)**2
    return s/(2*n)

#Calculate the cost function
def cost(n,a0,a1,x,y,ch,p=2):
    s=0;
    if ch=='sum-of-squares':
        for i in range(n):
            s+=(a0+a1*x[i]-y[i])**2
        return s/(2*n)
    if ch=='l-p norm':
        for i in range(n):
            s+=abs(a0+a1*x[i]-y[i])**p
        return s**(1/p)

#Partial Differential with respect to a0
def dela0(n,a0,a1,x,y):
    s=0;
    for i in range(n):
        s+=(a0+a1*x[i]-y[i])
    return s/n

#Partial Differential with respect to a1
def dela1(n,a0,a1,x,y):
    s=0;
    for i in range(n):
        s+=(a0+a1*x[i]-y[i])*x[i]
    return s/n

def predict(x, y, alphas=np.linspace(0.001,1,10), it=1000):
    mx=max(x)
    my=max(y)
    
    # Normalize values in the range 0-1
    for i in range(len(x)):
        x[i]/=mx
        y[i]/=my
    coeff, r2, cos = grad_desc(x, y, alphas, it)
    coeff, x, y = rescale(x, y, coeff, mx, my)
    r2_alpha(r2, alphas)
    plot_predict(x, y, coeff, r2, cos, it)
    # Store all predictions for which R^2 is maximum in an array
    a0=coeff[r2.index(max(r2))][0]
    a1=coeff[r2.index(max(r2))][1]
    pred=a0+x*a1
    return pred
    
def grad_desc(x, y, alphas, it):
    r2=[]# Array to store calculated R^2 values
    coeff=[] #Array to store Predicted Coefficients for Linear Regression
    
    for alpha in alphas:
        cos=[]
        #Initialize random weights
        a0=random.random()
        a1=random.random()
        for i in range(it):
            # Reduce the coefficient by alpha times partial differential
            temp0=a0-alpha*dela0(len(x),a0,a1,x,y)
            temp1=a1-alpha*dela1(len(x),a0,a1,x,y)
            a0=temp0
            a1=temp1
            #Add the cost for each iteration
            cos.append(cost(len(x),a0,a1,x,y,ch='sum-of-squares'))
        # Calculate and store the R^2 value for a particular learning rate alpha
        r2.append(1-(cos[-1]/(cos[-1]+sse(len(x),a0,a1,x,y))))
        #Store the predicted coefficients for regression
        coeff.append([a0,a1])
    return coeff, r2, cos
    
def r2_alpha(r2, alphas):
    #Plot for R^2 vs alpha
    plt.plot(alphas, r2)
    plt.title('R^2 vs. Learning Rate')
   
    #Max. value of R^2 over all values of alpha
    print(max(r2))
    #Value of alpha for maximum R^2
    print(np.linspace(0.001,1,10)[r2.index(max(r2))])
   
def rescale(x, y, coeff, mx, my):
    # Bring the data back to scale
    for i in range(len(coeff)):
        coeff[i][0]*=my
        coeff[i][1]*=my/mx
    for i in range(len(x)):
        x[i]*=mx
        y[i]*=my
    return coeff, x, y

def plot_predict(x, y, coeff, r2, cos, it):        
    # Plot the training data, cost function and Predicted vs Actual values
    fig1,ax=plt.subplots(1,2,figsize=(14,4))
    ax[0].plot([x for x in range(it)],cos)
    ax[0].set_title('Cost Function')
    ax[0].set_xlabel('No. of Iterations')
    ax[1].scatter(x,y,marker='x',color='r',label="Training Data")
    ax[1].plot(np.arange(1,12),[coeff[r2.index(max(r2))][0]+coeff[r2.index(max(r2))][1]*x for x in np.arange(1,12)],label="Linear Regression")
    plt.legend()
    ax[1].set_title('Predicted vs Actual')
    plt.xlabel("Experience in Years")
    plt.ylabel("Salary")
    plt.show()
