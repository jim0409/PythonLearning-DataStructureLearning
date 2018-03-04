import tensorflow as tf

a = tf.constant(10, name='a')
b = tf.constant(20, name='b')

y = tf.Variable(a + b * 2, name='y')

model = tf.initialize_all_variables()

with tf.Session() as session:
    merged = tf.merge_v2_checkpoints()
    writer = tf.train.SummarySaverHook()

