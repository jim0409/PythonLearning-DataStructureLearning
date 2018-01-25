import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import StatisticProblem.StatisticalInference.probabilityDistGen.myplotsetting as myplt


# def mypltSetting(xLabelName='', xFontsize=10, yLabelName='', yFontsize=10, titleName='no title'):
#     plt.title(titleName)
#     plt.xlabel(xLabelName, fontsize=xFontsize)
#     plt.ylabel(yLabelName, fontsize=yFontsize)


n = 10
p = 0.3
k = np.arange(0, 21)
binomial = stats.binom.pmf(k, n, p)
print(binomial)

plt.plot(k, binomial, 'o-')

titleName = 'Binomial: n =%i, p=%2f' % (n, p)

myplt.mypltSetting(xLabelName='Number of success', xFontsize=15, yLabelName='Probability of success', yFontsize=15,
             titleName=titleName)

plt.show()

# # .rvs函數模擬返回10000個參數為n,p的二項隨機變數
# binom_sim = stats.binom.rvs(n=10, p=0.3, size =10000)
#
# print("Mean :%g" % np.mean(binom_sim))
# print("SD: %g" % np.std(binom_sim, ddof=1))
# plt.hist(binom_sim, bins=10, normed=True) #normed
#
# mypltSetting(xLabelName='x',yLabelName='density')
# plt.show()
