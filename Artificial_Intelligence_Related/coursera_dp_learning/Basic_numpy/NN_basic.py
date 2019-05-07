# https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/2-6-np-concat/
import numpy as np

# apply with np lib to extend vector logit fun
def npSigmoid(x):
    s = 1/(1+np.exp(-x))
    return s

# GRADED FUNCTION: propagate
def propagate(w, b, X, Y):
    m = X.shape[1]
    # FORWARD PROPAGATION (FROM X TO COST)
    # A = np.Sigmoid(w*X + b)
    A = npSigmoid(np.dot(w.T, X) + b)

    cost1 = np.dot(Y, np.log(A).T)
    cost2 = np.dot((1 - Y), np.log(1 - A).T) /m
    cost = cost1 + cost2
    # cost = -np.sum(np.dot(Y, np.log(A).T) + np.dot((1 - Y), np.log(1 - A).T)) / m
    # BACKWARD PROPAGATION (TO FIND GRAD)
    dw = np.dot(X, (A - Y).T) / m
    db = np.sum((A - Y).T) / m
    cost = np.squeeze(cost)
    grads = {"dw": dw,
             "db": db}
    return grads, cost


def optimize(w, b, X, Y, num_iterations, learning_rate, print_cost=False):
    costs = []
    for i in range(num_iterations):
        grads, cost = propagate(w, b, X, Y)
        # Retrieve derivatives from grads
        dw = grads["dw"]
        db = grads["db"]
        # update rule
        w = w - learning_rate * dw
        b = b - learning_rate * db
        # Record the costs
        if i % 100 == 0:
            costs.append(cost)
        # Print the cost every 100 training examples
        if print_cost and i % 100 == 0:
            print("Cost after iteration %i: %f" % (i, cost))
    params = {"w": w,
              "b": b}
    grads = {"dw": dw,
             "db": db}
    return params, grads, costs

def predict(w, b, X):
    m = X.shape[1]
    Y_prediction = np.zeros((1, m))
    w = w.reshape(X.shape[0], 1)
    # Compute vector "A" predicting the probabilities of a cat being present in the picture
    A = npSigmoid(np.dot(w.T, X) + b)
    for i in range(A.shape[1]):
        # Convert probabilities A[0,i] to actual predictions p[0,i]
        if A[0, i] > 0.5:
            Y_prediction[0, i] = 1
        else:
            Y_prediction[0, i] = 0
        pass
    return Y_prediction

if __name__ == '__main__':
    # define training data
    menHeight = np.random.normal(175, 5, 100)
    menWeight = np.random.normal(65, 0.5, 100)
    womenHeight = np.random.normal(160, 5, 100)
    womenWeight = np.random.normal(50, 0.5, 100)
    inputX1 = np.hstack((menHeight,womenHeight))
    inputX2 = np.hstack((menWeight,womenWeight))
    inputX = np.vstack((inputX1,inputX2))
    trueY = np.hstack((np.repeat(1,100), np.repeat(0,100)))
    # trueY = trueY[:,np.newaxis]

    # training
    params, grads, costs = optimize(np.zeros(2)[:,np.newaxis], np.zeros(2)[:,np.newaxis], inputX, trueY, num_iterations=100, learning_rate=0.009, print_cost=False)

    # print out parms
    print(params)