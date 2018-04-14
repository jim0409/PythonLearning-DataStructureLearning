from __future__ import print_function
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


# use numpy to generate random exponential and feed it into placeholder
randExp1 = np.random.standard_exponential(100).reshape(1, 100)
randExp2 = np.random.standard_exponential(100).reshape(1, 100)

with tf.name_scope('input'):
    x1 = tf.placeholder(tf.float32, [None, 100], name="x1")
    x2 = tf.placeholder(tf.float32, [None, 100], name="x2")

with tf.name_scope('event'):
    event = x1 > x2
    with tf.name_scope('happen'):
        happen = tf.cast(event, tf.int32, name='happen')
    with tf.name_scope('freq'):
        freq = tf.reduce_mean(happen)
        tf.summary.scalar('freq', freq)

# with tf.name_scope('real_time'):

init = tf.global_variables_initializer()
merged = tf.summary.merge_all()

with tf.Session() as sess:
    sess.run(init)
    writer = tf.summary.FileWriter('./logs', sess.graph)
    for i in range(10):
        # obs_time = sess.run([merged, x], feed_dict={x: randExp})
        y1, y2 , _ = sess.run([merged, x1, x2], feed_dict={x1: randExp1, x2: randExp2})
        # print((y1>y2).astype(int))
        # print(y)
        # print(np.average(obs_time))

# sess = tf.Session()
# sess.run(init)
# y = sess.run(testVar, feed_dict={testVar: randExp})
# x = np.arange(len(y))

# print(y)


# also check the histogram plot
# plt.hist(y)
# plt.show()


# current_time = datetime(2018, 4, 6)
#
# a = db_writer.DBwriter(time=current_time, float_value=0.81, int_value=4)
# a.write()
