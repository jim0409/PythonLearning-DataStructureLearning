import tensorflow as tf
import matplotlib.pyplot as plt

# def random_normal(shape,
#                   mean=0.0,
#                   stddev=1.0,
#                   dtype=dtypes.float32,
#                   seed=None,
#                   name=None):
norm = tf.random_normal([100],mean=0,stddev=2)

with tf.Session() as session:
    plt.hist(norm.eval(),normed=True)
    plt.show()