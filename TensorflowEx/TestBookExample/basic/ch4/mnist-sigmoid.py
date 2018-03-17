from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import matplotlib.pyplot as plt

mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

# 設定訓練階段的epochs總數
training_epochs = 25

# 建立模型時需要的其他參數
learning_rate = 0.01
batch_szie = 100
display_step = 1

# 建立模型/設定權重矩陣以及誤差項
x = tf.placeholder("float", [None, 784])
y = tf.placeholder("float", [None, 10])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# 採用softmatrix矩陣來做激發函數
activation = tf.nn.softmax(tf.matmul(x, W) + b)

# 為了訓練模型的準確性，目標是調整權重矩陣Ｗ以及誤差項b致使模型預估值yhat與實際值y差異最小化
# 定義損失函數 cost
# cross_entropy : lostF = y*log(1-yhat)+(1-y)log(yhat)
cross_entropy = y * tf.log(activation)
cost = tf.reduce_mean(-tf.reduce_sum(cross_entropy, reduction_indices=1))

# 使用gradient descent方法求解最小化損失函數
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# 繪圖用x,y點座標，會以append的形式加入數列中
avg_set = []
epoch_set = []

# initialize variable
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    # 訓練開始
    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = int(mnist.train.num_examples / batch_szie)
        # loop over all batches
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_szie)
            # fit training using batch data
            sess.run(optimizer, feed_dict={x: batch_xs, y: batch_ys})
            # compute average loss
            avg_cost += sess.run(cost, feed_dict={x: batch_xs, y: batch_ys}) / total_batch

        # display logs per epoch step
        if epoch % display_step == 0:
            print("Epoch :", '%04d' % (epoch + 1), "cost =", "{:.9f}".format(avg_cost))

        avg_set.append(avg_cost)
        epoch_set.append(epoch + 1)

print("Training phase finished!")

plt.plot(epoch_set, avg_set, 'o', label='Logistic Regression Training phase')
plt.ylabel('cost')
plt.xlabel('epoch')
plt.legend()
plt.show()

# Test Model
# correct_prediction = tf.equal(tf.argmax(activation, 1), tf.argmax(y, 1))

# Calculate accuracy
# accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
# print("Model Accuragy:", accuracy({x: mnist.test.images, y: mnist.test.labels})))
