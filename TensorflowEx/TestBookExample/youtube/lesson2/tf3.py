import tensorflow as tf

# Fetch :
# execute multi operation in tensorflow in the same time
input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)

add = tf.add(input2, input3)
mul = tf.multiply(input1, add)

with tf.Session() as sess:
    # use [op1,op2, ...] means execute mult ops
    result = sess.run([mul, add])
    print(result)

# Feed
# use placeholder as a pre-variable in tensorflow
# not necessary to give vale while declaring
input4 = tf.placeholder(tf.float32)
input5 = tf.placeholder(tf.float32)
output = tf.multiply(input4, input5)

#
with tf.Session() as sess:
    # use feed.dict ;dictionary mode
    print(sess.run(output, feed_dict={input4: [7.0], input5: [2.0]}))
