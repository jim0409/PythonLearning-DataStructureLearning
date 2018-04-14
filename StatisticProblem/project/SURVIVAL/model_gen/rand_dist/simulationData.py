from __future__ import print_function
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# use numpy to generate random exponential and feed it into placeholder
randExp = np.random.standard_exponential(100).reshape(100,1).astype(np.float32)
testVar = tf.placeholder(dtype=tf.float32,name="testVar")

# also check the histogram plot

init = tf.global_variables_initializer()


sess = tf.Session()
sess.run(init)
y = sess.run(testVar,feed_dict={testVar:randExp})
x = np.arange(len(y))

plt.hist(y)
plt.show()
