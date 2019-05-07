#http://cpmarkchang.logdown.com/posts/193261-machine-learning-overfitting-and-regularization
import numpy as np
import matplotlib.pyplot as plt

x=np.matrix([[-1.        , -0.93103448, -0.86206897, -0.79310345, -0.72413793, -0.65517241,
              -0.5862069 , -0.51724138, -0.44827586, -0.37931034, -0.31034483, -0.24137931,
              -0.17241379, -0.10344828, -0.03448276,  0.03448276,  0.10344828,  0.17241379,
              0.24137931,  0.31034483,  0.37931034,  0.44827586,  0.51724138,  0.5862069 ,
              0.65517241,  0.72413793,  0.79310345,  0.86206897,  0.93103448,  1.        , ]])
y_train=np.matrix([[ 0.72679128,  0.88352371,  0.55848839,  0.9960148 ,  0.27727561,  1.58193644,
                     0.35519674,  0.40919248, -0.66450448, -1.02347355, -0.71433077, -0.97857498,
                     -0.9542627 , -0.85186192, -0.00210849, -0.00559543,  0.6545823 ,  0.82926143,
                     0.3728542 ,  1.60336863,  1.20548029, -0.20721056,  0.44713523, -0.49832341,
                     -0.34765828, -1.51883285, -0.95758709, -0.83135465, -0.90942741, -0.10016318, ]])
y_test=np.matrix([[ 0.79521635,  0.32523979,  0.63212171,  1.60522123,  0.72400525,  1.33408882,
                    -0.42555819, -0.19726661, -0.66041197, -0.65470685, -0.93661018, -0.87634342,
                    -0.84363868, -0.95689774, -0.1376653 ,  0.40842111, -0.20794503,  0.15057061,
                    0.50331016,  1.54413185,  0.01230807,  0.38623098,  0.32021572, -0.02133113,
                    -0.28643186, -0.91730531, -0.65369342, -0.68990553, -0.73800708, -0.56659495, ]])

def plot_data( y_model, title=''):
    plt.ion()
    fig, ax = plt.subplots()
    ax.plot(np.array([x[0,i]for i in range(x.shape[1])]) ,
            np.array([y_model[0,i]for i in range(y_model.shape[1])]) ,
            'k--')
    ax.plot(x, y_train, 'bo' )
    ax.plot(x, y_test, 'ro' )
    ax.set_xlim((-1, 1))
    ax.set_ylim((-2, 2))
    ax.set_title(title)
    plt.show()

def linear_regression(order):
    X = np.matrix([[x[0,j]**i for i in range(order) ] for j in range(x.shape[1])])
    w =  np.linalg.pinv( X )*y_train.T
    y_model = (X*w).T
    e_in = np.average(np.square(y_train - y_model))
    e_out = np.average(np.square(y_test - y_model))
    status_str = "Order=%s, Ein=%.6f, Eout=%.6f"%(order,e_in,e_out)
    print (status_str)
    plot_data(y_model , status_str)



