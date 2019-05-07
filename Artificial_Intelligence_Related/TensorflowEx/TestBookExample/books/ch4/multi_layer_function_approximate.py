import tensorflow as tf
import numpy as np
import math, random
import matplotlib.pyplot as plt

NUM_points = 1000
np.random.seed(NUM_points)

# 建立資料模型，要學習的函數將遵循餘弦(cos)函數的趨勢，從1000個點來評估
# 而在此會加入非常小的隨機誤差（雜訊）來模擬真實情況
function_to_learn = lambda x: np.cos(x) + 0.1 * np.random.rand(*x.shape)

# 建立MLP網路的隱藏層中有10個神經元
layer_1_neurons = 10

# 網路每次學習100個點，總共學習1500個學習週期（代）
batch_size = 100
NUM_EPOCHS = 1500

# 最後，建立訓練集和測試集
all_x = np.float32(np.random.uniform(-2 * math.pi, 2 * math.pi, (1, NUM_points))).T

np.random.shuffle(all_x)
train_size = int(900)

# 前900個是訓練集
x_training = all_x[:train_size]
y_training = function_to_learn(x_training)

# 後100個是驗證用的資料集合
x_validation = all_x[train_size:]
y_validation = function_to_learn(x_validation)

# 夠過matplotlib來顯示這些集合
plt.figure(1)
plt.scatter(x_training, y_training, c='blue', label='train')
plt.scatter(x_validation, y_validation, c='red', label='validation')
plt.legend()
# plt.show()

# build model
# first, define two placeholder X,Y
X = tf.placeholder(tf.float32, [None, 1], name='X')
Y = tf.placeholder(tf.float32, [None, 1], name='Y')

# create hidden layer [1X10]
# receive the value from input value
w_h = tf.Variable(tf.random_uniform([1, layer_1_neurons], minval=-1, maxval=1))
b_h = tf.Variable(tf.zeros([1, layer_1_neurons], dtype=tf.float32))

h = tf.nn.sigmoid(tf.matmul(X, w_h) + b_h)

# output layer would be a [10X1] tensor
w_o = tf.Variable(tf.random_uniform([layer_1_neurons, 1], minval=-1, maxval=1, dtype=tf.float32))
b_o = tf.Variable(tf.zeros([1, 1], dtype=tf.float32))

# 第二層的每一個神經元接收來自第一層神經元的輸入，結合連結的w_oij權重
# 並與輸出層相對應的偏差相加
model = tf.matmul(h, w_o) + b_o

# 在此使用的coss function為l2_loss
# 用來計算未sqrt的張量的L2標準的一半，即 output = sum((model-Y)**2)/2
train_op = tf.train.AdamOptimizer().minimize(tf.nn.l2_loss(model - Y))

# 啟動session
sess = tf.Session()
sess.run(tf.initialize_all_variables())
errors = []
for i in range(NUM_EPOCHS):
    for start, end in zip(range(0, len(x_training), batch_size), range(batch_size, len(x_training), batch_size)):
        sess.run(train_op, feed_dict={X: x_training[start:end], Y: y_training[start:end]})

    cost = sess.run(tf.nn.l2_loss(model - y_validation), feed_dict={X: x_validation})
    errors.append(cost)
    if i % 100 == 0:
        print("epoch %d, cost=%g" % (i, cost))

plt.figure(2)
plt.plot(errors,label='MLP Function Approximation')
plt.xlabel('epochs')
plt.ylabel('cost')
plt.legend()
plt.show()