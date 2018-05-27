import matplotlib.pyplot as plt
from tbrain.module.import_tfbrain_data import read_tbrain_data

startTime = '20180408'
endTime = '20180605'
codeNum = 50

def showDataTrend(x,y):
    plt.figure()
    plt.plot(x,y)
    plt.show()

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
                amplitude_signs.append(0)
            else:
                amplitude_signs.append(1)

    return amplitude_signs, diff_values

Df = read_tbrain_data('../data/taetfp.csv')  # 50 51 52
# Df = readData('../data/tasharep.csv')
# Df = readData('../data/tetfp.csv')
# Df = readData('../data/tsharep.csv')

trainDf = Df[(Df.code == codeNum)]



# 使用最近一兩年的資料
trainDf.index = trainDf.date
trainDF = trainDf[startTime:endTime]

# 找尋是否有趨勢
# showDataTrend(trainDF.date,trainDF.open)

# sample data if needed
# data = data[-20:]
data_amp, data_diff_values = calculate_amplitude(trainDF.open)
print(data_amp)
print('data length %d'%len(trainDf.date))
plt.plot(trainDF.date, data_diff_values,'ro')
plt.show()