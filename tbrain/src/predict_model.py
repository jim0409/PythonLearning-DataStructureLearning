import copy

import numpy as np
import tensorflow as tf

from tbrain.module.import_tfbrain_data import read_tbrain_data
from tbrain.module.lstm_model import LSTMRNN

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

Df = read_tbrain_data('../data/taetfp.csv')  # 50 51 52
# 使用code 50的data
trainDf = Df[(Df.code == 50)]

### check data tail

feed_data = copy.copy(trainDf[-355:-5])
true_value = trainDf[-5:].open.values.reshape(5, 1)

x_input = feed_data.close.values.reshape(35, 10, 1)


###

def show_diff(seq1, seq2, name):
    print("---diff : %s---" % name)
    print(seq2)
    print(seq1 - seq2)


def final_pred(pred, feed_data):
    global true_value
    openData = feed_data.open
    final_price = openData[-5:]
    final_std = np.std(openData[-5:])
    print(final_std)
    print(final_price)

    pred_result = (pred[-5:] * final_std + trainDf[-10:-5].close.values.reshape(5, 1))
    pred_result2 = (pred[-5:] * final_std + trainDf[-10:-5].open.values.reshape(5, 1))

    show_diff(true_value, pred_result, "pred1")
    show_diff(true_value, pred_result2, "pred2")

###
model = LSTMRNN(TIME_STEPS, INPUT_SIZE, OUTPUT_SIZE, CELL_SIZE, BATCH_SIZE, LEARNING_RATE)
saver = tf.train.Saver(tf.global_variables())
module_file = tf.train.latest_checkpoint(SAVING_DIR)
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    saver.restore(sess, module_file)

    feed_dict = {
        model.xs: x_input
    }

    pred = sess.run(model.pred, feed_dict=feed_dict)

    final_pred(pred, feed_data)