import numpy as np
import matplotlib.pyplot as plt
# logistic would be rewrite with numpy
from sklearn.linear_model import LogisticRegression

# purpose : use inverse cdf to get a pair data for women and men height, weight
# then use logistic reg to figure a parameter. Also, try with deep learning

# check scatter plot
def scatterPlot():
    plt.scatter(menHeight,menWeight,color="b")
    plt.scatter(womenHeight,womenWeight,color="r")
    plt.show()
    return 0
# logistic Regression
def trainLogisticRegression(trainX,trainY):
    logitReg=LogisticRegression()
    logitReg.fit(trainX,trainY)
    return logitReg
# check Distribution with histogram
def checkDist(sampleVector):
    plt.hist(sampleVector,20,normed=1, facecolor='blue', alpha=0.5)
    mu = sampleVector.mean().round(2)
    std = sampleVector.std().round(2)
    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Histogram of Dist: $\mu=' + str(mu) + '$, $\sigma=' + str(std) + '$')
    plt.show()
    return 0
# apply with np lib to extend vector logit fun
def npSigmoid(x):
    s = 1/(1+np.exp(-x))
    # return s
    print("Sigmoid(x) is "+ str(s))
# by inference use formula instead of scipy.mic.derivative to return ds
def sigmoidDerivative(x_vector):
    s = 1/(1+np.exp(-x_vector))
    ds = s*(1-s)
    # return ds
    print("sigmoid_derivative(x_vector) = " + str(ds))

# generate men height and weight with sex_term 1
menHeight = np.random.normal(175,5,100)
menWeight = np.random.normal(65,0.5,100)

# generate men height and weight with sex_term 0
womenHeight = np.random.normal(160,5,100)
womenWeight = np.random.normal(50,0.5,100)

# generate x_vector
x_vector = np.array([np.hstack([menWeight,womenWeight]),np.hstack([menHeight,womenHeight])])
y_true = np.hstack([np.ones(50),np.zeros(50)])

x_test = np.array([[x] for x in menHeight.tolist()])
# x_test = np.array([x] for x in menHeight)

test=LogisticRegression()
test.fit(x_test,y_true)
checkDist()

