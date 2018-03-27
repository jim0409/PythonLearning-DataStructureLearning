import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 載入數據庫
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

# 輸入圖片是28x28
n_inputs = 28  # 輸入一行，一行有28個數據
max_time = 28
lstm_size = 100
n_class = 10
batch_size = 50
n_batch = mnist.train.num_examples // batch_size

# 這裡的none表示第一個維度可以是任意的長度
x = tf.placeholder(tf.float32, [None, 784])
# 正確的標籤
y = tf.placeholder(tf.float32, [None, 10])

# 初始化權值
weights = tf.Variable(tf.truncated_normal([lstm_size, n_class]), stddev=0.1)
# 初始化偏量
biases = tf.Variable(tf.constant(0.1, shape=[n_class]))


# 定義RNN網路
def RNN(X, weights, biases):
    # inputs=[batch_size,max_time,n_inputs]
    inputs = tf.reshape(X, [-1, max_time, n_inputs])
    # 定義lstm基本cell
    # lstm_cell = tf.contrib.rnn.BasicLSTMCell(lstm_size)
    lstm_cell = tf.nn.rnn_cell.BasicLSTMCell(lstm_size)

    # final_state[0]是cell_state
    # final_state[1]是hidden_state
    outputs, final_state = tf.nn.dynamic_rnn(lstm_cell, inputs, dtype=tf.float32)
    results = tf.nn.softmax(tf.matmul(final_state[1], weights) + biases)
    return results


# 計算RNN的返回結果
prediction = RNN(x, weights, biases)
# 損失函數
cross_entorpy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=prediction, labels=y))
# 使用AdamOptimizer進行優化
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entorpy)
# 結果存放在一個布爾型列表中
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(prediction, 1))  # argmax返回一維張量中最大的值所在的位置
# 求準確率
accuracy = tf.reduce_mean(tf.case(correct_prediction, tf.float32))  # 把correct_prediction變為tf.float32類型
# 初始化
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for epoch in range(6):
        for batch in range(n_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})

        acc = sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels})
        print("Iter " + str(epoch) + ", Testing Accuracy= " + str(acc))
