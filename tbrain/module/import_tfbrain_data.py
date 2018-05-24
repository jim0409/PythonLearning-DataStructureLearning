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
