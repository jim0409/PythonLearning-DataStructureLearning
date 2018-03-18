# 多層感知器
# 一個更為複雜且又有效的架構是多層感知器（MLP,Multi Layer Perceptron)架構。
# 他基本上是由多層的感知器構成，並且至少存在一個不連接到輸入或輸出的隱藏層(hidden layer)

from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import matplotlib.pyplot as plt

mnist = input_data.read_data_sets("/tmp/data/",one_hot=True)

