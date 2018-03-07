import tensorflow as tf
import numpy as np

# use numpy random generate 100 points
x_data = np.random.rand(100)
y_data = x_data * 0.1 + 0.2

# create a linear model with slope b
b = tf.Variable(0.)
k = tf.Variable(0.)
y = k * x_data + b

# create a loss function ;mean_error square
loss = tf.reduce_mean(tf.square(y_data-y))

# define a gradient to optimise the trainer
optimizer = tf.train.GradientDescentOptimizer(0.2)

# train model
train = optimizer.minimize(loss)

# initial variable
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for step in range(201):
        sess.run(train)
        if step%20 ==0:
            print(step,sess.run([k,b]))