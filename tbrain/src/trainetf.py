import copy

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

from tbrain.module.lstm_model import LSTMRNN

BATCH_START = 0  # 定義batch開始處
TIME_STEPS = 10  # 每一層有幾個RNN - 定義10個工作天一層

# declaration global variable
final_pred_array = []
batch_averages = []
batch_stds = []


# normalization
def normalization(data):
    global final_average, final_std
    data_average = np.average(data)
    data_std = np.std(data)
    z_data = (data - data_average) / data_std

    batch_averages.append(data_average)
    batch_stds.append(data_std)

    return z_data


def get_batch(trainDf, BATCH_SIZE):
    global BATCH_START, TIME_STEPS
    start_pt = BATCH_START
    end_pt = BATCH_START + TIME_STEPS * BATCH_SIZE
    xs = np.array(copy.copy(trainDf.date[start_pt:end_pt]).reshape(BATCH_SIZE, TIME_STEPS))
    res = np.array(copy.copy(trainDf.open[1 + start_pt:1 + end_pt]).reshape(BATCH_SIZE, TIME_STEPS))
    res = normalization(res)
    seq = np.array(copy.copy(trainDf.open[start_pt:end_pt]).reshape(BATCH_SIZE, TIME_STEPS))
    seq = normalization(seq)

    BATCH_START += TIME_STEPS
    return [seq[:, :, np.newaxis], res[:, :, np.newaxis], xs]


def train_lstm(trainDf, TRAIN_LOOP, SAVING_DIR, INPUT_SIZE, OUTPUT_SIZE, CELL_SIZE, BATCH_SIZE, LEARNING_RATE):
    model = LSTMRNN(TIME_STEPS, INPUT_SIZE, OUTPUT_SIZE, CELL_SIZE, BATCH_SIZE, LEARNING_RATE)
    sess = tf.Session()
    merged = tf.summary.merge_all()
    # writer = tf.summary.FileWriter("logs", sess.graph)

    init = tf.global_variables_initializer()
    sess.run(init)
    saver = tf.train.Saver(tf.global_variables())

    # plt.ion()
    # plt.show()

    # 根據data量做調整，目前code 50有data 13XX
    # 能做迭代次數為 13XX/ (batch_size*step_size)
    for i in range(TRAIN_LOOP):
        seq, res, xs = get_batch(trainDf, BATCH_SIZE)
        if i == 0:
            feed_dict = {
                model.xs: seq,
                model.ys: res,
                # create initial state
            }
        else:
            feed_dict = {
                model.xs: seq,
                model.ys: res,
                model.cell_init_state: state  # use last state as the initial state for this run
            }

        _, cost, state, pred = sess.run(
            [model.train_op, model.cost, model.cell_final_state, model.pred],
            feed_dict=feed_dict)

        print('the %d_th cost: %.3f' % (i, round(cost, 4)))
        # result = sess.run(merged, feed_dict)

        # plotting
        # plt.plot(xs[0, :], res[0].flatten(), 'r', xs[0, :], pred.flatten()[:TIME_STEPS], 'b--')
        # plt.draw()
        # plt.pause(.3)

    saver.save(sess, SAVING_DIR + 'test.model.ckpt', global_step=96)

# def print_out_result():
#     global final_pred_array, final_res_array
# 顯示最後使用時間軸
# print(xs[-1:])
# final_pred_array = pred
# final_res_array = res

# 打印出平均數以及標準差
# print("the final_close average is ", batch_averages)
# print("the final_close std is ", batch_stds)
#
# print("the final pred_array is ", final_pred_array.flatten()[-TIME_STEPS * 2:])
# print("the final pred result is ", final_res_array.flatten()[-TIME_STEPS * 2:])
