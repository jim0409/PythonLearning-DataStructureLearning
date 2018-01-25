import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

rate = 2
n = np.arange(0, 10)
y = stats.poisson.pmf(n, rate)
print(y)

plt.plot(n, y)
plt.show()

# # 使用rvs作圖
# data = stats.poisson.rvs(mu=2, loc=0, size=1000)
# print("Mean: %g" % np.mean(data))
# print("SD: %g" % np.std(data, ddof=1))
#
# # 製作空圖
# plt.figure()
#
# plt.hist(data, bins=9, normed=True)
# plt.xlim(0,10)
# plt.xlabel("Number of accidents")
# plt.title("Simulating Poisson Random Variables")
# plt.show()
