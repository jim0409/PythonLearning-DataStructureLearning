import numpy as np
import tensorflow as tf
import copy
from tbrain.module.lstm_model import LSTMRNN


def show_diff(seq1, seq2, name):
    print("---diff : %s---" % name)
    print(seq2)
    print(seq2 - seq1)


def final_pred(pred, feed_data, trainDf, final_open_value):
    feed_x_input = feed_data.open
    final_feed_price = feed_x_input[-5:]
    final_feed_std = np.std(feed_x_input[-5:])
    print(final_feed_std)
    print(final_feed_price)
    print(final_open_value)

    pred_result = (pred[-5:] * final_feed_std + trainDf[-10:-5].close.values.reshape(5, 1))
    pred_result2 = (pred[-5:] * final_feed_std + trainDf[-10:-5].open.values.reshape(5, 1))

    show_diff(final_open_value, pred_result, "pred_open with close")
    show_diff(final_open_value, pred_result2, "pred_open with open")


def predict_lstm(trainDf, SAVING_DIR, TIME_STEPS, INPUT_SIZE, OUTPUT_SIZE, CELL_SIZE, BATCH_SIZE, LEARNING_RATE):
    ### check data tail
    feed_data = copy.copy(trainDf[-355:-5])
    final_open_value = trainDf[-5:].open.values.reshape(5, 1)
    x_input = feed_data.close.values.reshape(35, 10, 1)

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

    final_pred(pred, feed_data, trainDf, final_open_value)
