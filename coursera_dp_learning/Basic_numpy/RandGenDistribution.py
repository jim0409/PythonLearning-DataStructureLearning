import numpy as np
import matplotlib.pyplot as plt

n ,p = 10 ,0.5

s = np.random.binomial(n,p,100)

print(s)

plt.plot(range(100),s)
plt.show()

