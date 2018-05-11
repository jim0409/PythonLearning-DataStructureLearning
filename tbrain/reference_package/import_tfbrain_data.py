# -- coding: utf-8 --
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


# translate timestamp for matplotlib to plot
def trans_data_time(raw_data_times):
    data_times = []
    for ti in raw_data_times:
        ti = str(ti)
        year = int(ti[:4])
        month = int(ti[4:6])
        day = int(ti[6:8])
        data_time = datetime(year=year, month=month, day=day)
        data_times.append(data_time)
    return data_times


# rename the database cols' name
def data_pre_process(raw_data):
    # since the second col is needless chinese code
    raw_data.columns = ['code', 'date', 'c_code', 'open', 'max', 'min', 'close', 'deal']
    data = raw_data.drop(['c_code'], axis=1)
    data.iloc[:, 1] = trans_data_time(data.iloc[:, 1])
    return data


def read_tbrain_data(csv_data):
    raw_csv_ata = pd.read_csv(csv_data, encoding="ISO-8859-1")  # encoding with 'big5-hkscs' or 'ISO-88591-1'
    used_data = data_pre_process(raw_csv_ata)  # clean data
    return used_data


# for a better version should use [array] - [0,array[:len(array)-1]
def calculate_amplitude(data_price):
    diff_values = []
    amplitude_signs = []

    for i in range(len(data_price)):
        if i == 0:
            amplitude_signs.append(0)
            diff_values.append(0)
        else:
            diff_value = data_price[i] - data_price[i-1]
            diff_values.append(diff_value)
            if diff_value < 0:
                amplitude_signs.append(-1)
            else:
                amplitude_signs.append(1)

    return amplitude_signs, diff_values



# Df = read_tbrain_data('../data/taetfp.csv')  # 50 51 52
# Df = readData('../data/tasharep.csv')
# Df = readData('../data/tetfp.csv')
# Df = readData('../data/tsharep.csv')

# 0050/0051/0052


# 使用code 50的data
# data = Df[(Df.code == 59)]

# sample parts data
# data = data[-10:]
#
# # print(data.close.values)
# #
# data_amp, data_diff_values = calculate_amplitude(data.close.values)
#
# plt.plot(data.date, data.close)
# plt.figure()
# plt.plot(data.date, data_amp)
# plt.figure()
# plt.plot(data.date, data_diff_values)
#
#
# plt.show()
#
# print(len(data))
