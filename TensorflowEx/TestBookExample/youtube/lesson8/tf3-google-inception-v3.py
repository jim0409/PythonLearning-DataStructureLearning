import tensorflow as tf
import os
import tarfile
import requests

# define download url
inception_pretrain_model_url = "http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz"

# set a location for model placing
inception_pretrain_model_dir = "/tmp/inception_model"

# check whether the directory is under the path, if not ,create it
if not os.path.exists(inception_pretrain_model_dir):
    os.makedirs(inception_pretrain_model_dir)

# get file name and file location place
filename = inception_pretrain_model_url.split("/")[-1]
filepath = os.path.join(inception_pretrain_model_dir, filename)

# start downloading model
# check whether file 'filename' exists or not, if not ,download it
if not os.path.exists(filepath):
    print("download", filename)
    r = requests.get(inception_pretrain_model_url, stream=True)
    with open(filepath, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

print("finish", filename)

# unzip file
tarfile.open(filepath, 'r:gz').extractall(inception_pretrain_model_dir)

# create a folder for inception log
log_dir = '/tmp/inception_model/inception_log'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# ps: classify_image_graph_def.pb is a well-trained data by google
inception_graph_def_file = os.path.join(inception_pretrain_model_dir, 'classify_image_graph_def.pb')
with tf.Session() as sess:
    # create a graph to save google well-trained model
    with tf.gfile.FastGFile(inception_graph_def_file, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')
    # save graph
    writer = tf.summary.FileWriter(log_dir, sess.graph)
    writer.close()
