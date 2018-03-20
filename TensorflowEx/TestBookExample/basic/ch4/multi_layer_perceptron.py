# 多層感知器
# 一個更為複雜且又有效的架構是多層感知器（MLP,Multi Layer Perceptron)架構。
# 他基本上是由多層的感知器構成，並且至少存在一個不連接到輸入或輸出的隱藏層(hidden layer)

from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import matplotlib.pyplot as plt

mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

# 學習速率
learning_rate = 0.001

# 訓練代數
training_epochs = 2

# 設定要分類的圖像數量
batch_size = 100
display_step = 1

# 第一層神經元數量
n_hidden_1 = 256

# 第二層神經元數量
n_hidden_2 = 256

# 輸入的尺寸(每一張圖像為784像素):
n_input = 784  # 輸入MNIST資料(圖像為:28*28)

# 輸出的類別數
n_classes = 10

# 建立模型
x = tf.placeholder("float", [None, n_input])
y = tf.placeholder("float", [None, n_classes])

# 第一個隱藏層是由權重的h張量所構成，大小為[784,256]，其中256是該層的節點總數
h = tf.Variable(tf.random_normal([n_input, n_hidden_1]))
# 對於第一層定義的篇倀張量為
bias_layer_1 = tf.Variable(tf.random_normal([n_hidden_1]))
layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, h), bias_layer_1))

# 第二個中間層是以權重張量[256,256]的形狀來表示
w = tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2]))
bias_layer_2 = tf.nn.sigmoid(tf.random_normal([n_hidden_2]))
# 第二層的每個神經元是從layer 1的神經元接收輸入，與連接Wij相結合，並增加layer2相對應的偏差
layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, w), bias_layer_2))

# output layer
output = tf.Variable(tf.random_normal([n_hidden_2, n_classes]))
bias_output = tf.Variable(tf.random_normal([n_classes]))
output_layer = tf.matmul(layer_2, output) + bias_output

# 定義cost function
# tensorflow函數中tf.nn.softmax_cross_entropy_with_logits是計算softmax層的成本
# 他只會在訓練期間使用。logits是輸出模型的非標準化對數機率(在應用softmax標準化之前所輸出的值)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=output_layer, logits=y))

optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# condition setting
avg_set = []
epoch_set = []

# initial variable
init = tf.global_variables_initializer()

# 啟動圖形
with tf.Session() as sess:
    sess.run(init)
    # 定義週期
    for epoch in range(training_epochs):
        avg_cost = 0
        total_batch = int(mnist.train.num_examples / batch_size)
        # 對於所有的批次(100)執行迴圈
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            # 使用批次資料進行適當的訓練
            sess.run(optimizer, feed_dict={x: batch_xs, y: batch_ys})
            # 計算平均損失
            avg_cost += sess.run(cost, feed_dict={x: batch_xs, y: batch_ys}) / total_batch
            avg_set.append(avg_cost)
            epoch_set.append(epoch + 1)
    print("Training phase finished")

    # 最後測試MLP模型
    correct_prediction = tf.equal(tf.argmax(output_layer, 1), tf.argmax(y, 1))
    # 計算期準確性
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    test_acc =sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels})
    print("Model Accuracy:", test_acc)

    # 輸出訓練階段模型
    plt.plot(epoch_set, avg_set, 'o', label='MLP Training phase')
    plt.ylabel('cost')
    plt.xlabel('epoch')
    plt.legend()
    plt.show()



# tf.cast用法
# tf.eval用法
# tf.exec用法
# http://www.cnblogs.com/yyds/p/6276746.html