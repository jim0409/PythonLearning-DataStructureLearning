#first_session_only_tensorflow.py
import tensorflow as tf

x = tf.constant(1, name='x')
y = tf.Variable(x + 9, name='y')

# model = tf.initialize_all_variables()
model =tf.global_variables_initializer()


with tf.Session() as session:
    # session.extend would be used to extend execution graph wihle calculating
    # session.run is the main process of programing
    session.run(model)
    print(session.run(y))