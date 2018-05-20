import copy

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

from tbrain.module.import_tfbrain_data import read_tbrain_data
from tbrain.module.lstm_model import LSTMRNN

# read raw data
Df = read_tbrain_data('../data/taetfp.csv')  # 50 51 52
# 使用code 50的data
trainDf = Df[(Df.code == 50)]

# read parameter config
BATCH_START = 0  # 定義batch開始處
TIME_STEPS = 10  # 每一層有幾個ＲＮＮ - 定義10個工作天一層
BATCH_SIZE = 35  # 定義每次batch提出的量的大小
INPUT_SIZE = 1  # 放入參數個數
OUTPUT_SIZE = 1  # 輸出參數個數
CELL_SIZE = 10  # 多少個hidden units
LEARNING_RATE = 0.006  # 學習率
TRAIN_LOOP = 96  # 迭代次數
SAVING_DIR = '/Users/jimweng/PythonLearning-DataStructureLearning/tbrain/src/save_model/'

model = LSTMRNN(TIME_STEPS, INPUT_SIZE, OUTPUT_SIZE, CELL_SIZE, BATCH_SIZE, LEARNING_RATE)

# check saving_dir
print(SAVING_DIR)

# check data tail
testData = copy.copy(trainDf[-350:].close)
openData = copy.copy(trainDf[-350:].open)

final_average = (openData[-6:-1])
final_std = np.std(openData[-6:-1])

saver = tf.train.Saver(tf.global_variables())

module_file = tf.train.latest_checkpoint(SAVING_DIR)

init = tf.global_variables_initializer()

x_input = testData.reshape(35, 10, 1)
with tf.Session() as sess:
    sess.run(init)
    saver.restore(sess, module_file)

    feed_dict = {
        model.xs: x_input
    }

    pred = sess.run(model.pred, feed_dict=feed_dict)

    print(final_std, final_average)
    final_average = np.average(final_average)
    print(pred[-6:-1] * final_std*final_std)
    plt.plot(pred[-6:-1] * final_std + final_average)
    plt.show()
