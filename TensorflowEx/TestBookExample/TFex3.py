import numpy as np
import tensorflow as tf

# convert 1 dimension to tensor
tensor_1d = np.array([1, 2, 3, 4, 2.3])
tf_tensor = tf.convert_to_tensor(tensor_1d, dtype=tf.float64)

with tf.Session() as sess:
    print(sess.run(tf_tensor))
    print(sess.run(tf_tensor[0]))
    print(sess.run(tf_tensor[1]))
