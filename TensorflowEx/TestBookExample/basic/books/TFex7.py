# gradient

import tensorflow as tf

# define a place holder
x = tf.placeholder(tf.float32)

# define a math function y=x^2
y = 2 * x * x

# implement y and x into tf.gradients()
var_grad = tf.gradients(y, x)

# build a session to calculate
with tf.Session() as session:
    var_grad_val = session.run(var_grad, feed_dict={x: 1})  # given x=1

print(var_grad_val)  # 4.0
