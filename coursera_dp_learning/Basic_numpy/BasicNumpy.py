import math
import numpy as np
import matplotlib.pyplot as plt
# Create a rD*cD_matrix with each element between lowerBound and upperBound
# random int  : randArray = np.random.randint(lowerBound,upperBound,(rowDim,colDim))
# Create a rD*cD_matrix with each element between [0,1)
# random float: randArray = np.random.rand(rowDim,colDim)
# Create a uniform rD*cD_matrix with each element between [a,b)
# random unif : randUnif  = np.random.uniform(low = a, high = b , size = None)
print("----2017/11/05-----")
# basic logit fun for sigmoid value
def valueSigmoid(x):
    s = 1/(1+math.exp(-x))
    # return s
    print("Sigmoid value is " + str(s))
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

# Generate a random vector
# x_vector = np.array([1, 2, 3])
x_vector = np.random.uniform(-1,1,1000)
print(x_vector)

count, bins, ignored = plt.hist(x_vector,20,normed=True)
plt.plot(x_vector,np.ones_like(x_vector),linewidth=1,color='r')
plt.show()

# print out value sigmoid : valueSigmoid(x_vector[0])
# print out npSigmoid : npSigmoid(x_vector)
# print out sigmoidDerivative : sigmoidDerivative(x_vector)