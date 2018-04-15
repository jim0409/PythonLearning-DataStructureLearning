# through this file, i start my generation from pre-define model scale
# using inverse cdf theory to generate a survival time via coxph-transformed model
# then store data into influxdb and visualize it with grafana

import os
import sys
import configparser
import argparse
import logging
import numpy as np
import tensorflow as tf
from datetime import datetime
from influxdb import InfluxDBClient

sample_config = """
[FitModel]
Model = "Linear"
number_of_points = 500

[Linear-Parameters]
slope = 0.22
intercept = 0.78
"""

logging.basicConfig(level=logging.INFO)


class LinearSimulation():
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
        return self.__ai_value, self.__stat_value


class DBwriter():
    def __init__(self, time, ai_value, stat_value, true_value):
        self.__time = time
        self.__ai_value = ai_value
        self.__stat_value = stat_value
        self.__true_value = true_value

    def write(self):
        self.__time = self.strftime()
        self.dbwriter()
        return 0

    def strftime(self):
        return self.__time.strftime('%Y-%m-%dT%H:%M:%SZ')

    def dbwriter(self, host='localhost', port=8086):
        """Instantiate a connection to the InfluxDB."""
        user = 'root'
        password = 'root'
        dbname = "demo"
        hostname = "jim_test_server"
        region = "taiwan"
        measurement = "surf"
        json_body = [
            {
                "measurement": measurement,
                "tags": {
                    "host": hostname,
                    "region": region
                },

                "time": self.__time,
                "fields": {
                    "ai_value": self.__ai_value,
                    "stat_value": self.__stat_value,
                    "true_value": self.__true_value,
                }
            }
        ]

        client = InfluxDBClient(host, port, user, password, dbname)

        logging.info("Create database: " + dbname)
        client.create_database(dbname)

        logging.info("Write points: {0}".format(json_body))
        client.write_points(json_body)
        return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', type=str, help='need to insert an valid conf file')
    parser.add_argument('-s', '--sample_config', type=str, help='use --sample_config true to see config')
    opts = parser.parse_args()

    if opts.sample_config == 'true':
        print(sample_config)
        sys.exit(1)
    else:
        pass

    if opts.config is None:
        logging.info("need to put a valid conf")
        sys.exit(1)
    else:
        if not os.path.isfile(opts.config):
            print("file doesn't exist")
        else:
            config = configparser.ConfigParser()
            config.read(opts.config)
            configFile = config['FitModel']
            conf1 = configFile.get('Model')
            if conf1 is not None:
                if conf1.split('"')[1] != "Linear":
                    logging.info("only support Linear model now!")
                    sys.exit(1)
                else:
                    conf2 = config['Linear-Parameters']
                    logging.info("Use " + conf1 + " model to generate data")
                    if conf2 is not None:
                        slope = conf2.getfloat('slope')
                        intercept = conf2.getfloat('intercept')
                        logging.info("with parameter slope %0.3f and intercept %0.3f" % (slope, intercept))
                        return slope, intercept


if __name__ == '__main__':
    current_time = datetime(2018, 4, 15)

    slope, intercept = main()
    linearModel = LinearSimulation(time=current_time, a=slope, b=intercept)
    aiValue, statValue = linearModel.estimator_ai()
    dbwriter = DBwriter(time=current_time, ai_value=aiValue, stat_value=statValue, true_value=slope)
    dbwriter.write()
