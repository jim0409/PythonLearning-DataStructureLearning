import numpy as np

# define loss function with sum_i | yhat_i - y_i |
def lossFunction1(yhat,y):
    loss = np.sum(np.abs(yhat-y),keepdims=True)
    return loss

# define loss function with sum_i (yhat_i - y_i )*(yhat_i - y_i )
def lossFunction2(yhat,y):
    loss = np.sum((yhat-y)*2)
    return loss

# random generate estimator yhat_i and y_i
yhat_i = np.random.randint(low=0,high=100,size=10)/100
y_i = np.random.random_integers(low=0,high=1,size=10)

print(yhat_i)
print(y_i)
print("-------------")
print('lossfunction1 ',lossFunction1(yhat_i,y_i))
print('lossfunction2 ',lossFunction2(yhat_i,y_i))