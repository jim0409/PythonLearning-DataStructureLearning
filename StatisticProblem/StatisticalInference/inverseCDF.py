# http://python.jobbole.com/81321/
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def mypltSetting(xLabelName,xFontsize,yLabelName,yFontsize,titleName):
    plt.title(titleName)
    plt.xlabel(xLabelName,fontsize=xFontsize)
    plt.ylabel(yLabelName,fontsize=yFontsize)

# random exponential
randomSurvivalTime = np.random.exponential(scale=1)

print(randomSurvivalTime)

n = 10
p = 0.3
k = np.arange(0,21)
binomial = stats.binom.pmf(k,n,p)
print(binomial)

plt.plot(k,binomial,'o-')

titleName='Binomial: n =%i, p=%2f'%(n,p)

mypltSetting(xLabelName='Number of success',xFontsize=15,yLabelName='Probability of success',yFontsize=15,titleName=titleName)

# plt.title('Binomial: n =%i, p=%2f'%(n,p),fontsize=15)
# plt.xlabel('Number of success')
# plt.ylabel('Probability of success',fontsize=15)

plt.show()

