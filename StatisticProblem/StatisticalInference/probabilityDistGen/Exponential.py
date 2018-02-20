import numpy as np
import matplotlib.pyplot as plt
import StatisticProblem.StatisticalInference.probabilityDistGen.myplotsetting as myplt

lambd = 0.5

x = np.arange(0, 15, 0.1)
y = lambd * np.exp(-lambd * x)  # could also use stats.expon.pdf
plt.plot(x, y)

myplt.mypltSetting(titleName='Exponential: $\lambda$ =%.2f' % lambd, xLabelName='x', yLabelName='Probability density')

plt.show()


# https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.exponential.html
# np.random.exponential(1/landa ,sampleSzie)