import numpy as np

# total_series_length = 50000
# echo_step = 3
# batch_size = 5


# gen time series data trend
def generateData(total_series_length, echo_step, batch_size):
    x = np.array(np.random.choice(2, total_series_length, p=[0.5, 0.5]))
    y = np.roll(x, echo_step)
    y[0:echo_step] = 0
    x = x.reshape((batch_size, -1))  # The first index changing slowest, subseries as rows
    y = y.reshape((batch_size, -1))
    return (x, y)


# data = generateData(total_series_length, echo_step, batch_size)
# print(data)
