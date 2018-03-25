# https://www.tensorflow.org/versions/r1.1/get_started/embedding_viz
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.contrib.tensorboard.plugins import projector

# read data set
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

# running times
max_steps = 1001

# number of pictures(maximum 10000)
image_num = 3000

# set size for each batch
# batch_size = 100

# access path
DIR = '/home/ubuntu/tensorboard/'

# create a Seesion()
sess = tf.Session()

# load image
# use method stack :
embedding = tf.Variable(tf.stack(mnist.test.images[:image_num]), trainable=False, name='embedding')

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

with tf.name_scope('input_reshape'):
    # transform x(placeholder) -1 (means unsure variable) 28 28 (28*28) 1 (1-dimension)
    image_shaped_input = tf.reshape(x, [-1, 28, 28, 1])
    # use summary_image to pass pic into tensorboard
    tf.summary.image('input', image_shaped_input, 10)

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
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(loss)

# initial global variable/ not necessary to name it, it has default name
init = tf.global_variables_initializer()

with tf.name_scope('accuracy'):
    # tf.argmax = indicator (y ,{y >1)} ;1 ,else}
    with tf.name_scope('correct_prediction'):
        # save result in a bool table
        correct_prediction = tf.equal(tf.argmax(y, 1),
                                      tf.argmax(prediction, 1))  ## argmax return the maximun in the tensor

    # calculate the accuracy
    with tf.name_scope('accuracy'):
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        tf.summary.scalar('accuracy', accuracy)

# generate Meta Data
if tf.gfile.Exists(DIR + 'projector/projector/metadata.csv'):
    tf.gfile.DeleteRecursively(DIR + 'projector/projector/metadata.csv')
with open(DIR + 'projector/projector/metadata.csv', 'w') as f:
    # argmax: find maximum in an array, would tag with 1 instead other values would be 0
    labels = sess.run(tf.argmax(mnist.test.labels[:], 1))
    for i in range(image_num):
        f.write(str(labels[i]) + '\n')

# merge all summary
merged = tf.summary.merge_all()

projector_writer = tf.summary.FileWriter(DIR + 'projector/projector/metadata.csv', sess.graph)
saver = tf.train.Saver()
config = projector.ProjectorConfig()
embed = config.embeddings.add()
embed.tensor_name = embedding.name
embed.metadata_path = DIR + 'projector/projector/metadata.csv'
embed.sprite.image_path = DIR + 'projector/data/mnist_10k_sprite.png'
embed.sprite.single_image_dim.extend([28, 28])
projector.visualize_embeddings(projector_writer, config)

for i in range(max_steps):
    # for each 100 batch_size
    batch_xs, batch_ys = mnist.train.next_batch(100)
    run_options = tf.RunOptions(trace_level=tf.RunOptions.FULL_TRACE)
    run_metadata = tf.RunMetadata()
    summary, _ = sess.run([merged, train_step], feed_dict={x: batch_xs, y: batch_ys}, options=run_options,
                          run_metadata=run_metadata)
    projector_writer.add_run_metadata(run_metadata, 'step%03d' % i)
    projector_writer.add_summary(summary, i)

    if i % 100 == 0:
        acc = sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels})
        print("Iter " + str(i) + ", Testing Accuracy= " + str(acc))

saver.save(sess, DIR + 'projector/projector/a_model.ckpt', global_step=max_steps)
projector_writer.close()
sess.close()

