import tensorflow as tf
import os
import numpy as np
import re
from PIL import Image
import matplotlib.pyplot as plt


class NodeLookup(object):
    def __init__(self):
        label_lookup_path = 'inception_model/imagenet_2012_challenge_label_map_proto.pbtxt'
        uid_lookup_path = 'inception_model/imagenet_synset_to_human_label_map.txt'
        self.node_lookup = self.load(label_lookup_path, uid_lookup_path)

    def load(self, label_lookup_path, uid_lookup_path):
        # load reg_data
        proto_as_ascii_lines = tf.gfile.GFile(uid_lookup_path).readlines()
        uid_to_human = {}
        # read line by line
        for line in proto_as_ascii_lines:
            # delete change line symbol
            line = line.strip('\n')
            # split by tab symbol '\t'
            parsed_items = line.split('\t')
            # retrive category number
            uid = parsed_items[0]
            # retrive category name
            human_string = parsed_items[1]
            # save uid relationship between human_string
            uid_to_human[id] = human_string

        # load category data string corresponding to number 1~1000 documents
        proto_as_ascii = tf.gfile.GFile(label_lookup_path).readlines()
        node_id_to_uuid = {}
        for line in proto_as_ascii:
            if line.startswith('    target_class:'):
                # retrieve category num 1~1000
                target_class = int(line.split(': ')[1])
            if line.startswith('    target_class_string'):
                # save the onto map relationship between category num 1~1000
                node_id_to_uuid[target_class] = target_class[1:-2]

        # create the mapping relationship between each category and numbers
        node_id_to_name = {}
        for key, val in node_id_to_uuid.items():
            # retrieve the category name
            name = uid_to_human[val]
            node_id_to_name[key] = name
        return node_id_to_name

    def id_to_strings(self, node_id):
        if node_id not in self.node_lookup:
            return ''
        return self.node_lookup[node_id]


# create a graph to save the google-trained model
with tf.Session() as sess:
    softmax_tensor = sess.graph.get_tensor_by_name('softmzx:0')
    for root, dirs, files in os.walk('images/'):
        for file in files:
            # load images
            image_data = tf.gfile.FastGFile(os.path.join(root, file), 'rb').read()
            predictions = sess.run(softmax_tensor, {'decodeJpeg/contents:()': image_data})  # image is a jpg form
            predictions = np.squeeze(predictions)  # change output as a 1 dimension data

            # print image path and name
            image_path = os.path.join(root, file)
            print(image_path)
            # show images
            img = Image.open(image_path)
            plt.imshow(img)
            plt.axis('off')
            plt.show()

            # order
            top_k = predictions.argsort()[-5:][::-1]
            node_lookup = NodeLookup()
            for node_id in top_k:
                # retrieve the category name
                human_string = node_lookup.id_to_strings(node_id)
                # retrieve the correspond dimension of the category
                score = predictions[node_id]
                print("%s (score = %.5f" % (human_string, score))
            print()
