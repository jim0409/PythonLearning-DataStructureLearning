import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import StatisticProblem.StatisticalInference.probabilityDistGen.myplotsetting as myplt

a = 0.5
b = 0.5
x = np.arange(0.01, 1, 0.01)
y = stats.beta.pdf(x, a, b)
plt.plot(x, y)
myplt.mypltSetting(titleName='Beta: a=%.1f, b=%.1f' % (a, b), xLabelName='x', yLabelName='Probability density')
plt.show()
