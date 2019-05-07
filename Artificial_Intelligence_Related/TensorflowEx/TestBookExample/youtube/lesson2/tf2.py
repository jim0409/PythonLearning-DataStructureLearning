import tensorflow as tf

x = tf.Variable([1, 2])
a = tf.Variable([3, 3])

# add a minus operation
sub = tf.subtract(x, a)

# add a plus operation
add = tf.add(x, sub)

# initial needed
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(sub))
    print(sess.run(add))

# create a variable with initial value 0
state = tf.Variable(0, name='counter')
state2 = tf.Variable(10, name='counter2')

# create an operation to count state
new_value = tf.add(state, 1)
new_value2 = tf.subtract(state2, 1)

# give value operate
update = tf.assign(state, new_value)
update2 = tf.assign(state2, new_value2)

# initialize variable
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    # print(sess.run(state))
    for _ in range(5):
        sess.run(state)
        sess.run(state2)
        print("----")
        print(sess.run(update2))
        print(sess.run(update))
