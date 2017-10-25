import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0.,4.,0.1)
print(t)
print(type(t))
plt.plot(t,t,t,t+2,t,t**2)
plt.show()