import tensorflow as tf
from tbrain.module.lstm_model import LSTMRNN
from tbrain.src.train_model import SAVING_DIR_FILE_NAME
from tbrain

with tf.Session() as sess:
    model = LSTMRNN(TIME_STEPS, INPUT_SIZE, OUTPUT_SIZE, CELL_SIZE, BATCH_SIZE, LEARNING_RATE)
    saver = tf.train.Saver()
    saver.restore(sess, SAVING_DIR_FILE_NAME)
    print(sess.run())