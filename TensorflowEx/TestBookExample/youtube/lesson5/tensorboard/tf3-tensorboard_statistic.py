import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# read data set
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

# set size for each batch
batch_size = 100

# calculate how many batch in this example
n_batch = mnist.train.num_examples // batch_size


# parameter setting
def variabe_summary(var):
    with tf.name_scope('summaries'):
        mean = tf.reduce_mean(var)
        tf.summary.scalar('mean', mean)  # average
    with tf.name_scope('stdev'):
        stdev = tf.sqrt(tf.reduce_mean(tf.square(var - mean)))
    tf.summary.scalar('stdev', stdev)  # standard deviation
    tf.summary.scalar('max', tf.reduce_max(var))  # maximum
    tf.summary.scalar('min', tf.reduce_min(var))  # minimum
    tf.summary.histogram('histogram', var)  # histogram


# to visualize need to have an namespace
with tf.name_scope('input'):
    # define two placeholder
    x = tf.placeholder(tf.float32, [None, 784], name='x-input')
    y = tf.placeholder(tf.float32, [None, 10], name='y-input')

# create a simple neural network
with tf.name_scope('layer'):
    with tf.name_scope('weights'):
        W = tf.Variable(tf.zeros([784, 10]), name='W')
        variabe_summary(W)
    with tf.name_scope('bias'):
        b = tf.Variable(tf.zeros([10]), name='bias')
        variabe_summary(b)
    with tf.name_scope('wx_plus_b'):
        wx_plus_b = tf.matmul(x, W) + b
    with tf.name_scope('softmax'):
        prediction = tf.nn.softmax(wx_plus_b)

# define loss function
# loss = tf.reduce_mean(tf.square(y - prediction))
with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y, logits=prediction))
    tf.summary.scalar('loss', loss)  # since the statistic of loss is too few to need use our func variable_summary

# use gradient descent method
with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.2).minimize(loss)

# initial global variable/ not necessary to name it, it has default name
init = tf.global_variables_initializer()

with tf.name_scope('accuracy'):
    # tf.argmax = indicator (y ,{y >1)} ;1 ,else}
    # save result in a bool table
    with tf.name_scope('correct_prediction'):
        correct_prediction = tf.equal(tf.argmax(y, 1),
                                      tf.argmax(prediction, 1))  ## argmax return the maximun in the tensor

    # calculate the accuracy
    with tf.name_scope('accuracy'):
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        tf.summary.scalar('accuracy', accuracy)

# merge all summary
merged = tf.summary.merge_all()

with tf.Session() as sess:
    sess.run(init)
    # '/path' could be assign free
    writer = tf.summary.FileWriter('./logs/tf3/logs', sess.graph)
    # out cycle with 21 iterator
    for epoch in range(21):
        # inner cycle to calculate for n_batch times
        for batch in range(n_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            # execute both merged and train_step
            summary, _ = sess.run([merged, train_step], feed_dict={x: batch_xs, y: batch_ys})

            writer.add_summary(summary, epoch)
        acc = sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels})
        print("iter " + str(epoch) + " ,Testing Accuracy " + str(acc))

