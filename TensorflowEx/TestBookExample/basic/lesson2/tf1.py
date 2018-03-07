import tensorflow as tf

# create a constant operation
m1 = tf.constant([[3,3]])

# create a constant operation
m2 = tf.constant([[2],[3]])

# create an multiplier operation and put m1,m2
product =  tf.matmul(m1,m2)
print((product))

# define a Session to start up
sess = tf.Session()

# use sees.run to execute the matrix multiplier
result = sess.run(product)
print(result)

sess.close()

# also can use with method
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)