import numpy as np


# apply with np lib to extend vector logit fun
def npSigmoid(x):
    s = 1/(1+np.exp(-x))
    return s
# by inference use formula instead of scipy.mic.derivative to return ds
def sigmoidDerivative(x_vector):
    s = 1/(1+np.exp(-x_vector))
    ds = s*(1-s)
    return ds


# GRADED FUNCTION: propagate
def propagate(w, b, X, Y):


    m = X.shape[1]

    # FORWARD PROPAGATION (FROM X TO COST)
    ### START CODE HERE ### (≈ 2 lines of code)
    A = sigmoid(np.dot(w.T, X) + b)  # compute activation
    cost = -np.sum(np.dot(Y, np.log(A).T) + np.dot((1 - Y), np.log(1 - A).T)) / m  # compute cost
    ### END CODE HERE ###

    # BACKWARD PROPAGATION (TO FIND GRAD)
    ### START CODE HERE ### (≈ 2 lines of code)
    dw = np.dot(X, (A - Y).T) / m
    db = np.sum((A - Y).T) / m
    ### END CODE HERE ###


    cost = np.squeeze(cost)

    grads = {"dw": dw,
             "db": db}

    return grads, cost
