import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# use numpy to generate 200 random points
x_data = np.linspace(-0.5, 0.5, 200)[:, np.newaxis]
noise = np.random.normal(0, 0.02, x_data.shape)

y_data = np.square(x_data + noise)

# define other two place holders
# 'None' would be replace while the shape be insert (e.g. x_data with shape 200)
x = tf.placeholder(tf.float32, [None, 1])
y = tf.placeholder(tf.float32, [None, 1])

# given one varaible x get an answer of y
# output layer would be a variable y
# hidden layer would be included ten neural

# define the hidden layer
# weight matrix
Weights_L1 = tf.Variable(tf.random_normal([1, 10]))
# noise matrix
bias_L1 = tf.Variable(tf.zeros([1, 10]))
# weight matrix with noise
Wx_plus_b_L1 = tf.matmul(x, Weights_L1) + bias_L1
L1 = tf.nn.tanh(Wx_plus_b_L1)

# define output layer
# weight matrix
Weights_L2 = tf.Variable(tf.random_normal([10,1]))
# noise matrix
bias_L2 = tf.Variable(tf.zeros([1, 1]))
# weight matrix with noise
Wx_plus_b_L2 = tf.matmul(L1, Weights_L2) + bias_L2

prediction = tf.nn.tanh(Wx_plus_b_L2)

# define loss function and trainning method
# loss function would be root mean square error
loss = tf.reduce_mean(tf.square(y-prediction))

# use gradient descient method
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# Start Session
with tf.Session() as sess:
    # initialize global variables
    sess.run(tf.global_variables_initializer())
    for _ in range(2000):
        sess.run(train_step,feed_dict={x:x_data,y:y_data})

    # get prediction value
    prediction_value = sess.run(prediction,feed_dict={x:x_data})

    # show picture
    plt.figure()
    plt.scatter(x_data,y_data)

    # r: red color ; -: with line type - ; and lw: means the width of line
    plt.plot(x_data,prediction_value,'r-',lw =5)
    plt.show()