from __future__ import print_function, division
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tbrain.module.simulation_data import generateData
from tbrain.module.plot import plot

# config parameters
num_epochs = 3
total_series_length = 50000
truncated_backprop_length = 15
state_size = 4
num_classes = 2
echo_step = 3
batch_size = 5
num_batches = total_series_length // batch_size // truncated_backprop_length

# build-model
batchX_placeholder = tf.placeholder(tf.float32, [batch_size, truncated_backprop_length])
batchY_placeholder = tf.placeholder(tf.int32, [batch_size, truncated_backprop_length])
init_state = tf.placeholder(tf.float32, [batch_size, state_size])

# RNN layer designed (2)
# With First Layer Weight matrix (dim : 5x4 ;since state_size is 4), bias matrix ( dim : 1x4 )
W = tf.Variable(np.random.rand(state_size + 1, state_size), dtype=tf.float32)  # randomly initialize weights
b = tf.Variable(np.zeros((1, state_size)), dtype=tf.float32)  # anchor, improves convergence, matrix of 0s
# With Second Layer Weight matrix (dim : 4x2 ; since num_classes is 2), bias matrix (dim : 1x2 )
W2 = tf.Variable(np.random.rand(state_size, num_classes), dtype=tf.float32)
b2 = tf.Variable(np.zeros((1, num_classes)), dtype=tf.float32)

inputs_series = tf.unstack(batchX_placeholder, axis=1)
labels_series = tf.unstack(batchY_placeholder, axis=1)

# Forward pass
# state placeholder
current_state = init_state
states_series = []

# for each set of inputs
# forward pass through the network to get new state value
# store all states in memory
for current_input in inputs_series:
    # format input; from origin [batch_size,]<unstack> to [batch_size, 1]<reshape>
    current_input = tf.reshape(current_input, [batch_size, 1])
    # mix both state and input data
    input_and_state_concatenated = tf.concat([current_input, current_state], 1)  # Increasing number of columns
    # perform matrix multiplication between weights and input, add bias
    # squash with a non-linearity, for probability value
    next_state = tf.tanh(tf.matmul(input_and_state_concatenated, W) + b)  # Board casted addition
    # store the state in memory
    states_series.append(next_state)
    # set current state to next one
    current_state = next_state

# calculate loss
logits_series = [tf.matmul(state, W2) + b2 for state in states_series]  # Broadcasted addition
# apply softmax nonlinearity for output probability
predictions_series = [tf.nn.softmax(logits) for logits in logits_series]

# with the softmax cross entropy loss.
losses = [tf.nn.sparse_softmax_cross_entropy_with_logits(labels=labels, logits=logits) for logits, labels in
          zip(logits_series, labels_series)]
# #computes average, one value
total_loss = tf.reduce_mean(losses)
train_step = tf.train.AdagradOptimizer(0.3).minimize(total_loss)

# Step 3 Training the network
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # interactive mode
    plt.ion()
    # initialize the figure
    plt.figure()
    # show the graph
    plt.show()
    # to show the loss decrease
    loss_list = []

    for epoch_idx in range(num_epochs):
        # generate data at every epoch, batches run in epochs
        x, y = generateData(total_series_length=total_series_length,
                            echo_step=echo_step,
                            batch_size=batch_size)
        # initialize an empty hidden state
        _current_state = np.zeros((batch_size, state_size))

        print("New data, epoch", epoch_idx)
        # each batch
        for batch_idx in range(num_batches):
            # starting and ending point per batch
            # since weights reoccuer at every layer through time
            # These layers will not be unrolled to the beginning of time,
            # that would be too computationally expensive, and are therefore truncated
            # at a limited number of time-steps
            start_idx = batch_idx * truncated_backprop_length
            end_idx = start_idx + truncated_backprop_length

            batchX = x[:, start_idx:end_idx]
            batchY = y[:, start_idx:end_idx]

            # run the computation graph, give it the values
            # we calculated earlier
            _total_loss, _train_step, _current_state, _predictions_series = sess.run(
                [total_loss, train_step, current_state, predictions_series],
                feed_dict={
                    batchX_placeholder: batchX,
                    batchY_placeholder: batchY,
                    init_state: _current_state
                })

            loss_list.append(_total_loss)

            if batch_idx % 100 == 0:
                print("Step", batch_idx, "Loss", _total_loss)
                plot(loss_list, _predictions_series, batchX, batchY, truncated_backprop_length)

plt.ioff()
plt.show()
