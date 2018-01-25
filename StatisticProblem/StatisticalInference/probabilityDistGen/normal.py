import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import StatisticProblem.StatisticalInference.probabilityDistGen.myplotsetting as myplt

mu = 0
sigma = 1
x = np.arange(-5, 5, 0.1)

y = stats.norm.pdf(x, 0, 1)

# note : $\mu$ is symbol of mean

myplt.mypltSetting(xLabelName='x', yLabelName='Probability', titleName='Normal: $\mu$=%.1f, $\sigma^2$=%.1f' % (mu, sigma))

plt.plot(x, y)
plt.show()
