import math
import numpy as np

# basic logit fun for sigmoid value
def basicSigmoid(x):
    s = 1/(1+math.exp(-x))
    return s

# apply with np lib to extend vector logit fun
def npSigmoid(x):
    # s = np.zeros(len(x))
    s = 1/(1+np.exp(-x))
    return s

# by inference use formula instead of scipy.mic.derivative to return ds
def sigmoidDerivative(x):
    s = 1/(1+np.exp(-x))
    ds = s*(1-s)
    return ds

# print out basic sigmoid
x = 1
print(basicSigmoid(x))

# print out npSigmoid
x_vector = np.array([1,2,3])
print(npSigmoid(x_vector))

# print out sigmoidDerivative
x_ds = np.array([1, 2, 3])
print ("sigmoid_derivative(x) = " + str(sigmoidDerivative(x_ds)))

# generate a series of random number between (0/1)
# Method 1 : random gen float and round()
# randNum = np.random.rand(20).round()
# Method 2 : random gen int between 0 & 1
# randNum = np.random.randint(0,2,(1,20))
# print(type(randNum))
# print(randNum)