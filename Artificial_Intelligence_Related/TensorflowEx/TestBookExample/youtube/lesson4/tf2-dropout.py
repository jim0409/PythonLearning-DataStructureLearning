import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# read data set
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

# set size for each batch
batch_size = 100

# calculate how many batch in this example
n_batch = mnist.train.num_examples // batch_size

# define two placeholder
x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

keep_prob = tf.placeholder(tf.float32)

# create a simple neural network
W1 = tf.Variable(tf.truncated_normal([784, 2000], stddev=0.1))
b1 = tf.Variable(tf.zeros([2000]) + 0.1)
L1 = tf.nn.tanh(tf.matmul(x, W1) + b1)
# keep_prob 可以設定多少百分比的神經元在工作
L1_drop = tf.nn.dropout(L1, keep_prob)

W2 = tf.Variable(tf.truncated_normal([2000, 2000], stddev=0.1))
b2 = tf.Variable(tf.zeros([2000]) + 0.1)
L2 = tf.nn.tanh(tf.matmul(L1_drop, W2) + b2)
# keep_prob 可以設定多少百分比的神經元在工作
L2_drop = tf.nn.dropout(L2, keep_prob)

W3 = tf.Variable(tf.truncated_normal([2000, 1000], stddev=0.1))
b3 = tf.Variable(tf.zeros([1000]) + 0.1)
L3 = tf.nn.tanh(tf.matmul(L2_drop, W3) + b3)
# keep_prob 可以設定多少百分比的神經元在工作
L3_drop = tf.nn.dropout(L3, keep_prob)

W4 = tf.Variable(tf.truncated_normal([1000, 10], stddev=0.1))
b4 = tf.Variable(tf.zeros([10]) + 0.1)

prediction = tf.nn.softmax(tf.matmul(L3_drop, W4) + b4)

# define loss function
# loss = tf.reduce_mean(tf.square(y - prediction))
# 改用交叉商做代價函數
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y, logits=prediction))

# use gradient descent method
# Optimizer can be AdamOptimizer or others
# e.g.
# train_step = tf.train.AdamOptimizer(1e-2).minimize(loss)
train_step = tf.train.GradientDescentOptimizer(0.2).minimize(loss)

# initial global variable
init = tf.global_variables_initializer()

# tf.argmax = indicator (y ,{y >1)} ;1 ,else}
# save result in a bool table
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(prediction, 1))  ## argmax return the maximun in the tensor

# calculate the accuracy
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(init)
    # out cycle with 21 iterator
    for epoch in range(21):
        # inner cycle to calculate for n_batch times
        for batch in range(n_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys, keep_prob: 1.0})

    test_acc = sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels, keep_prob: 1.0})
    train_acc = sess.run(accuracy, feed_dict={x: mnist.train.images, y: mnist.train.labels, keep_prob: 1.0})
    print("iter " + str(epoch) + " ,Testing Accuracy " + str(test_acc) + " ,Training Accuracy " + str(train_acc))
