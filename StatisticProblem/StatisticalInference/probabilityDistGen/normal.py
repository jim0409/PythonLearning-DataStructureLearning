import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import StatisticProblem.StatisticalInference.probabilityDistGen.myplotsetting as myplt

mu = 0
sigma = 1
x = np.arange(-5, 5, 0.1)

y = stats.norm.pdf(x, 0, 1)


# def mypltSetting(xLabelName='', xFontsize=10, yLabelName='', yFontsize=10, titleName='no title'):


myplt.mypltSetting()

plt.plot(x, y)
plt.show()

