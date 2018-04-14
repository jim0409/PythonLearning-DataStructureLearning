from __future__ import print_function
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import StatisticProblem.project.SURVIVAL.db.influxdb.db_writer.influxdb_writer as db_writer


def variable_summaries(var):
    """Attach a lot of summaries to a Tensor (for TensorBoard visualization)."""
    with tf.name_scope('summaries'):
        mean = tf.reduce_mean(var)
        tf.summary.scalar('mean', mean)
        with tf.name_scope('stddev'):
            stddev = tf.sqrt(tf.reduce_mean(tf.square(var - mean)))
        tf.summary.scalar('stddev', stddev)
        tf.summary.scalar('max', tf.reduce_max(var))
        tf.summary.scalar('min', tf.reduce_min(var))
        tf.summary.histogram('histogram', var)



# use numpy to generate random exponential and feed it into placeholder
randExp = np.random.standard_exponential(100).reshape(100, 1).astype(np.float32)
with tf.name_scope('testVar'):
    testVar = tf.placeholder(dtype=tf.float32, name="testVar")
    variable_summaries(testVar)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)
writer = tf.summary.FileWriter('./logs',sess.graph)
y = sess.run(testVar, feed_dict={testVar: randExp})
x = np.arange(len(y))

print(y)






# also check the histogram plot
# plt.hist(y)
# plt.show()


# current_time = datetime(2018, 4, 6)
#
# a = db_writer.DBwriter(time=current_time, float_value=0.81, int_value=4)
# a.write()
