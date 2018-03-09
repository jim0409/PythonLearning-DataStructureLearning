# mandelbrot set (not work)
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

y, x = np.mgrid[-1.3:1.3:0.005, -2:1:0.005]
z = x + 1j * y
c = tf.constant(z.astype(np.complex64))

zs = tf.Variable(c)

ns = tf.Variable(tf.zeros_like(c, tf.float32))

sess = tf.InteractiveSession()
tf.initialize_all_tables().run()

zs_ = zs * zs + c
not_diverged = tf.complex(zs_) < 4
step = tf.group(zs.assign(zs_), ns.assign_add(tf.cast(not_diverged, tf.float32)))
for i in range(200): step.run()
plt.imshow(ns.eval())
plt.show()
