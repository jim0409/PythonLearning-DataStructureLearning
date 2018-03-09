import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# load data set
mnis = input_data.read_data_sets("MNIST_data",one_hot=True)

# set batch size
batch_size = 100

# calculate number of batch
n_batch = mnis.train.num_examples // batch_size

# define two place holder 784 = 28*28
x = tf.placeholder(tf.float32,[None,784])
y = tf.placeholder(tf.float32,[None,10])

# create a simple neural network
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

prediction = tf.nn.softmax(tf.matmul(x,W)+b)