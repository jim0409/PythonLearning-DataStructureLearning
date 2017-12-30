import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression


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
    return s

# by inference use formula instead of scipy.mic.derivative to return ds
def sigmoidDerivative(x_vector):
    s = 1/(1+np.exp(-x_vector))
    ds = s*(1-s)
    return ds

# generate men height and weight with sex_term 1
menHeight = np.random.normal(175,5,100)
menWeight = np.random.normal(65,0.5,100)

# generate men height and weight with sex_term 0
womenHeight = np.random.normal(160,5,100)
womenWeight = np.random.normal(50,0.5,100)

# generate x_vector
x_vector=[]
for index in range(0,len(menWeight)):
    x_vector.append([menWeight[index],menHeight[index]])

for index in range(0, len(menWeight)):
    x_vector.append([womenWeight[index],womenHeight[index]])

y_true = np.hstack([np.ones(100),np.zeros(100)])

logistReg=LogisticRegression()
logistReg.fit(x_vector,y_true)

print('coef = ', logistReg.coef_ , ' intercept = ',logistReg.intercept_)

# e.g. a person with height 175 and weight 65 has the probability of men would be
print(npSigmoid(65*logistReg.coef_[0][0]+175*logistReg.coef_[0][1]+logistReg.intercept_[0]))

