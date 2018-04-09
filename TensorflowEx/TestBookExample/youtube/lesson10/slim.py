# 多任務學習標籤
# multi-task learning聯合訓練集
# 1.下載tensorflow提供的slim套件（備註：裡面提供的tensorflow套件非官方維護之package故可能有問題）
# 2.修改套件內的alexnet
# 3.使用該套件內涵括的package nets_factory

import os
import tensorflow as tf
from PIL import Image
from tensorflow.contrib.slim.nets import alexnet
import numpy as np
from models.research.slim.nets.nets_factory import get_network_fn

# 不同字符數量
CHAR_SET_LEN = 10
# 圖片高度
IMAGE_HEIGHT = 60
# 圖片寬度
IMAGE_WIDTH = 160
# 批次
BATCH_SIZE = 25
# tfrecord文件存放路徑
TFRECORD_FILE = "."

# placeholder
x = tf.placeholder(tf.float32, [None, 224, 224])
y0 = tf.placeholder(tf.float32, [None])
y1 = tf.placeholder(tf.float32, [None])
y2 = tf.placeholder(tf.float32, [None])
y3 = tf.placeholder(tf.float32, [None])

# 學習率
lr = tf.Variable(0.003, dtype=tf.float32)


# 從tfrecord讀出數據
def read_and_decode(filename):
    # 根據文件生成一個陣列
    filename_queue = tf.train.string_input_producer([filename])
    reader = tf.TFRecordReader()
    # 返回文件名和文件
    _, serialized_example = reader.read(filename_queue)
    features = tf.parse_single_example(serialized_example,
                                       features={
                                           'image': tf.FixedLenFeature([], tf.string),
                                           'label0': tf.FixedLenFeature([], tf.int64),
                                           'label1': tf.FixedLenFeature([], tf.int64),
                                           'label2': tf.FixedLenFeature([], tf.int64),
                                           'label3': tf.FixedLenFeature([], tf.int64),
                                       })
    # 獲取圖片數據
    image = tf.decode_raw(features['image'], tf.uint8)
    # tf.train shuffle_batch必須確認shape
    image = tf.reshape(image, [224, 224])
    # 圖片預處理
    image = tf.cast(image, tf.float32) / 255.0
    image = tf.subtract(image, 0.5)
    image = tf.multiply(image, 2.0)
    # 獲取label
    label0 = tf.cast(features['label0'], tf.int32)
    label1 = tf.cast(features['label0'], tf.int32)
    label2 = tf.cast(features['label0'], tf.int32)
    label3 = tf.cast(features['label0'], tf.int32)

    return image, label0, label1, label2, label3


# 獲取圖片數據和標籤
image, label0, label1, label2, label3 = read_and_decode(TFRECORD_FILE)

# 使用shuffle_batch可以隨機打亂
image_batch, label_batch0, label_batch1, label_batch2, label_batch3 = tf.train.shuffle_batch(
    [image, label0, label1, label2, label3], batch_size=BATCH_SIZE,
    capacity=50000, min_after_dequeue=10000, num_threads=1)

# 定義網絡結構
train_network_fn = get_network_fn('alexnet_v2', num_classes=CHAR_SET_LEN, weight_decay=0.0005, is_training=True)

with tf.Session() as sess:
    # inputs: a tensor of size [batch_size, height, width, channels]
    X = tf.reshape(x, [BATCH_SIZE, 224, 224, 1])
    # 數據輸入網路得到輸出值
    logits0, logits1, logits2, logits3, end_points = train_network_fn(X)

    # 把標籤轉乘one_hot的形式
    one_hot_labels0 = tf.one_hot(indices=tf.cast(y0, tf.int32), depth=CHAR_SET_LEN)
    one_hot_labels1 = tf.one_hot(indices=tf.cast(y0, tf.int32), depth=CHAR_SET_LEN)
    one_hot_labels2 = tf.one_hot(indices=tf.cast(y0, tf.int32), depth=CHAR_SET_LEN)
    one_hot_labels3 = tf.one_hot(indices=tf.cast(y0, tf.int32), depth=CHAR_SET_LEN)

    # 計算loss
    loss0 = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits0, labels=one_hot_labels0))
    loss1 = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits1, labels=one_hot_labels1))
    loss2 = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits2, labels=one_hot_labels2))
    loss3 = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits3, labels=one_hot_labels3))

    # 計算總的loss
    total_loss = (loss0 + loss1 + loss2 + loss3) / 4.0

    # 優化total_loss
    optimizer = tf.train.AdamOptimizer(learning_rate=lr).minimize(total_loss)

    # 計算準確率
    correct_prediction0 = tf.equal(tf.argmax(one_hot_labels0, 1), tf.argmax(logits0, 1))
    accuracy0 = tf.reduce_mean(tf.cast(correct_prediction0, tf.float32))

    correct_prediction1 = tf.equal(tf.argmax(one_hot_labels1, 1), tf.argmax(logits1, 1))
    accuracy1 = tf.reduce_mean(tf.cast(correct_prediction1, tf.float32))

    correct_prediction2 = tf.equal(tf.argmax(one_hot_labels2, 1), tf.argmax(logits2, 1))
    accuracy2 = tf.reduce_mean(tf.cast(correct_prediction2, tf.float32))

    correct_prediction3 = tf.equal(tf.argmax(one_hot_labels3, 1), tf.argmax(logits3, 1))
    accuracy3 = tf.reduce_mean(tf.cast(correct_prediction3, tf.float32))

    # 用於保存模型
    saver = tf.train.Saver()
    # 初始化
    sess.run(tf.global_variables_initializer())

    # 創建一個協調器，管理線程
    coord = tf.train.Coordinator()
    # 啟動QueueRunner，此時文件名稱已經進隊
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    for i in range(21):
        # 獲取一個批次的數據和標籤
        b_image, b_label0, b_label1, b_label2, b_label3 = sess.run([image_batch, label_batch0, label_batch1,
                                                                    label_batch2, label_batch3])
        # 模型優化
        sess.run(optimizer, feed_dict={x: b_image, y0: b_label0, y1: b_label1, y2: b_label2, y3: b_label3})

        # 每迭代20次計算一次loss和準確率
        if i% 20 ==0:
            # 每迭代2000次降低一次學習率
            if i % 2000 == 0:
                sess.run(tf.assign(lr,lr/3))
            acc0 ,acc1, acc2, acc3, loss_ =sess.run([accuracy0, accuracy1, accuracy2, accuracy3],feed_dict={x :b_image,
                                                                                                            y0:b_label0,
                                                                                                            y1:b_label1,
                                                                                                            y2:b_label2,
                                                                                                            y3:b_label3})
            learning_rate = sess.run(lr)
            print("Iter:%d Losss:%d.3f Accuracy:%d.2f,%d.2f,%d.2f,%d.2f Learning_rate:%d.4f"%(i,loss_,acc0,acc1,acc2,acc3,learning_rate))

            # 保存模型在相對路徑./captcha/models/crack_capt下
            # if acc > 0.90 and acc1 > 0.90 and acc2 > 0.90 and acc3 > 0.90:
            if i == 6000:
                saver.save(sess,"./captcha/models/crack_capt.model",global_step=i)

    # 通知其他線程關閉
    coord.request_stop()
    # 其他所有縣城關閉之後，這一函數才能返回
    coord.join(threads)