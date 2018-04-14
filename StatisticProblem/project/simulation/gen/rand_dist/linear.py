import numpy as np
import tensorflow as tf
from StatisticProblem.project.simulation.db.influxdb.db_writer.influxdb_writer import DBwriter

from datetime import datetime
# current_time = datetime(2018, 4, 15)
# #
# # number_of_points = 500
# #
# #
# # ai_diff = 0
# # stat_diff = 0
# #
# a = 0.22
# b = 0.78


class LinearSimulation:
    def __init__(self, time, a, b, number_of_points=500, ai_value=0, stat_value=0):
        self.__time = time
        self.__a = a
        self.__b = b
        self.__number_of_points = number_of_points
        self.__ai_value = ai_value
        self.__stat_value = stat_value

    def estimator_ai(self):
        x_point = []
        y_point = []
        for i in range(self.__number_of_points):
            x = np.random.normal(0.0, 0.5)
            y = self.__a * x + self.__b + np.random.normal(0.0, 0.1)
            x_point.append([x])
            y_point.append([y])
        self.__stat_value = np.average(y_point)
        with tf.name_scope('input'):
            A = tf.Variable(tf.random_uniform([1], -1.0, 1.0), name='x-input')
            B = tf.Variable(tf.zeros([1]), name='bias')
        with tf.name_scope('prediction'):
            y = A * x_point + B
        with tf.name_scope('loss'):
            loss_func = tf.reduce_mean(tf.square(y - y_point), name='mse')
        optimizer = tf.train.GradientDescentOptimizer(0.5)
        train = optimizer.minimize(loss_func)
        init = tf.global_variables_initializer()
        with tf.Session() as sess:
            sess.run(init)
            writer = tf.summary.FileWriter('./logs', sess.graph)
            for step in range(21):
                sess.run(train)
            self.__ai_value = sess.run(B)[0]

    def writedb(self):
        a = DBwriter(time=self.__time, ai_value=self.__ai_value, stat_value=self.__stat_value,
                               true_value=self.__b)
        a.write()


# a = LinearSimulation(time=current_time, a=a, b=b)
# a.estimator_ai()
# a.writedb()
