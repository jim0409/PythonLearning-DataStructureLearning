# http://python.jobbole.com/81321/
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# random exponential
randomSurvivalTime = np.random.exponential(scale=1)

print(randomSurvivalTime)

n = 10
p = 0.3
k = np.arange(0,21)
binomial = stats.binom.pmf(k,n,p)
binomial

plt.plot(k,binomial,'o-')
plt.title('Binomial: n =%i, p=%2f'%(n,p),fontsize=15)
plt.xlabel('Number of success')
plt.ylabel('Probability of success',fontsize=15)
plt.show()