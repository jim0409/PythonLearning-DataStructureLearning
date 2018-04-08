import tensorflow as tf
import os
import random
import math
import sys
from PIL import Image
import numpy as np

# 驗證集數量
_NUM_TEST = 500

# 隨機種子
_RANDOM_SEED = 0

# 數據集路徑: 路徑將會依據tf1生成的驗證碼所存放的地點
DATASET_DIR = "./captcha/"

# tfrecord 文件存放路徑
TFRECORD_DIR = "./tf2-captcha-result/"


# 判斷tfrecord文件是否存在
def _dataset_exists(dataset_dir):
    for split_name in ['train', 'test']:
        output_filename = os.path.join(dataset_dir, split_name + '.tfrecords')
        if not tf.gfile.Exists(output_filename):
            return False
    return True


# 獲取所有驗證碼圖片
def _get_filenames_and_classes(dataset_dir):
    photo_filenames = []
    for filenames in os.listdir(dataset_dir):
        # 獲取文件路徑
        path = os.path.join(dataset_dir, filenames)
        photo_filenames.append(path)
    return photo_filenames


def int64_feature(values):
    if not isinstance(values, (tuple, list)):
        values = [values]
    return tf.train.Feature(int64_list=tf.train.Int64List(value=values))


def bytes_feature(values):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[values]))


def image_to_tfexample(image_data, label0, label1, label2, label3):
    # Abstract base class for protocol messages.
    return tf.train.Example(features=tf.train.Features(feature={
        'image': bytes_feature(image_data),
        'label0': int64_feature(label0),
        'label1': int64_feature(label1),
        'label2': int64_feature(label2),
        'label3': int64_feature(label3),
    }))


# 把數據轉為TFRecord格式
def _convert_dataset(split_name, filenames, dataset_dir):
    assert split_name in ['train', 'test']

    with tf.Session() as sess:
        # 定義tfrecord文件的路徑＋名字
        output_filename = os.path.join(TFRECORD_DIR, split_name + '.tfrecords')
        with tf.python_io.TFRecordWriter(output_filename) as tfrecord_writer:
            for i, filename in enumerate(filenames):
                try:
                    sys.stdout.write('\r>>Converting image %d\%d' % (i + 1, len(filenames)))
                    sys.stdout.flush()

                    # 讀取圖片
                    image_data = Image.open(filename)
                    # 根據模型的結構resize
                    image_data = np.array(image_data.convert('L'))
                    # 將圖片轉化為bytes
                    image_data = image_data.tobytes()

                    # 獲取label
                    labels = filename.split('/')[-1][0:4]
                    num_labels = []
                    for j in range(4):
                        num_labels.append(int(labels[j]))
                    # 生成protocol數據模型
                    example = image_to_tfexample(image_data, num_labels[0], num_labels[1], num_labels[2], num_labels[3])
                    tfrecord_writer.write(example.SerializeToString())
                except IOError as e:
                    print("Could not read:", filename)
                    print("Error:", e)
                    print("Skip it\n")
    sys.stdout.write('\n')
    sys.stdout.flush()


# 判斷tdrecord文件是否存在
if _dataset_exists(TFRECORD_DIR):
    print("tfrecord文件已存在")
else:
    # 獲取所有圖片
    photo_filenames = _get_filenames_and_classes(DATASET_DIR)

    # 把數據切分為訓練集和測試集，並打亂
    random.seed(_RANDOM_SEED)
    random.shuffle(photo_filenames)
    training_filenames = photo_filenames[_NUM_TEST:]
    testing_filenames = photo_filenames[:_NUM_TEST]

    # 數據轉換
    _convert_dataset('train', training_filenames, DATASET_DIR)
    _convert_dataset('test', testing_filenames, DATASET_DIR)
    print('生成tfcecord文件')
