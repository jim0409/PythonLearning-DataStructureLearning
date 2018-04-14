import numpy as np
import tensorflow as tf
from datetime import datetime
import StatisticProblem.project.SURVIVAL.db.influxdb.db_writer.influxdb_writer as db_writer

number_of_points = 500

x_point = []
y_point = []

ai_diff = 0
stat_diff = 0

a = 0.22
b = 0.78

for i in range(number_of_points):
    x = np.random.normal(0.0, 0.5)
    y = a * x + b + np.random.normal(0.0, 0.1)
    x_point.append([x])
    y_point.append([y])

with tf.name_scope('input'):
    A = tf.Variable(tf.random_uniform([1], -1.0, 1.0), name='x-input')
    B = tf.Variable(tf.zeros([1]), name='bias')

with tf.name_scope('prediction'):
    y = A * x_point + B

with tf.name_scope('cost-fun'):
    cost_function = tf.reduce_mean(tf.square(y - y_point), name='mean-square-error')

optimizer = tf.train.GradientDescentOptimizer(0.5)

with tf.name_scope('train'):
    train = optimizer.minimize(cost_function)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    writer = tf.summary.FileWriter('./logs', sess.graph)
    for step in range(0, 21):
        sess.run(train)
    ai_value = sess.run(B)[0]

stat_value = np.mean(y_point).astype(np.float32)

print(ai_value, stat_value)

current_time = datetime(2018, 4, 6)


a = db_writer.DBwriter(time=current_time, ai_value=ai_value, stat_value=stat_value, true_value=b)
a.write()
