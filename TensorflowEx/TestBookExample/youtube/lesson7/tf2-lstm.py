import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 載入數據庫
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

# 輸入圖片是28x28
n_inputs = 28 # 輸入一行，一行有28個數據
max_time = 28
lstm_size = 100
n_class = 10
batch_size = 50
n_batch = mnist.train.num_examples // batch_size