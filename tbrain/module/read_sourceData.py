import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# if the difference is abnormal would like to print info ...
def checkDifference(difference_value, index):
    return print(date_x[index], difference_value)

data = pd.read_csv('../data/test.csv')

date = data['date'].values.astype(str)
y = data['open'].values


# transfer datetime - would like to adjust datetime as yyyy-mm-dd
date_x = []
for x in date:
    year = int(x[:4])
    month = int(x[4:6])
    day = int(x[6:8])
    test = datetime(year=year, month=month, day=day)
    date_x.append(test)

state = []
diff_array = []
for i in range(len(y)):
    if i == 0:
        state.append(0)
        diff_array.append(0)
    else:
        difference = y[i] - y[i - 1]
        diff_array.append(difference)
        if abs(difference) > 1:
            checkDifference(difference,i)
        if difference <0 :
            state.append(-1)
        else:
            state.append(1)

# plt.plot(date_x, y)

plt.plot(diff_array)
plt.show()

