import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

# 每個批次的大小
batch_size = 100

# 計算一共有多少個批次
n_batch = mnist.train.num_examples // batch_size


# 初始化權值
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)  # 生成一個截斷的常態分配
    return tf.Variable(initial)


# 初始化偏量
def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


# 卷積層
def conv2d(x, W):
    # x input tensor of shape '[batch, in_height, in_width, in_channels]'
    # W filter /kernel tensor of shape [filter_height, filter_width, in_channels, out_channels]
    # strides[0] = strides[3]=1, strides[1]代表x方向的布長, strides[0]代表y方向的布長
    # padding: A string from: 'SAME', 'VALID'
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


# 池化層
def max_pool_2x2(x):
    # ksize [1,x,y,1]
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


# 定義兩個placeholder
x = tf.placeholder(tf.float32, [None, 784])  # 28x28
y = tf.placeholder(tf.float32, [None, 10])

# 改變x的格式轉為4D的向量[batch, in_height, in_width, in_channels]
x_image = tf.reshape(x, [-1, 28, 28, 1])

# 初始化第一個卷積層的權值和偏量
W_conv1 = weight_variable([5, 5, 1, 32])  # 採用5x5的採樣窗口，32個卷積核從1個平面抽取特徵
b_conv1 = bias_variable([32])  # 每一個卷積核一個偏量

# 把x_image和權值向量進行卷積，再加上偏量值，然後應用於relu激活函數
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)  # 執行max-pooling

# 初始化第二個卷積層的權值和偏量
W_conv2 = weight_variable([5, 5, 32, 64])  # 採用5x5的採樣窗口，64個卷積核從32個平面抽取特徵
b_conv2 = bias_variable([64])  # 每一個卷積核一個偏量

# 把x_image和權值向量進行卷積，再加上偏量值，然後應用於relu激活函數
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)  # 執行max-pooling

# 28x28 的圖片第一次卷積後還是28x28，第一次池化後變為14x14
# 第二次卷積後為14x14，第二次池化後變為7x7
# 透過上面操作後得到64張7x7的平面

# 初始化第一個全聯接層的權值
W_fc1 = weight_variable([7 * 7 * 64, 1024])  # 上一張有7*7*64個神經元，全連結層有1024個神經元
b_fc1 = bias_variable([1024])  # 1024個節點

# 把池化層2的輸出層平化為1維
h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
# 求第一個全連接層的輸出
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

# keep_prob用來表示神經元的輸出機率
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# 初始化第二個全聯接層的權值
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

# 計算輸出
prediction = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

# 交叉熵代價函數
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y, logits=prediction))
# 使用AdamOptimizer進行優化
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
# 結果存放在一個布爾列表中
correct_prediction = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))  # argmax返回一維張亮中最大的值所在的位置
# 求準確率
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(21):
        for batch in range(n_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys, keep_prob: 0.7})

        acc = sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels, keep_prob: 1.0})
        print("Iter " + str(epoch) + ". Testing Accuracy= " + str(acc))
