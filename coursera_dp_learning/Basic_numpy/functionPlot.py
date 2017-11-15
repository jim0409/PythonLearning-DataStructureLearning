import numpy as np
import matplotlib.pyplot as plt

# define logist function
def npSigmoid(x):
    s = 1/(1+np.exp(-x))
    return s

# np.array => np.exp (make sure np with numpy structure as ndarray)
x = np.array([-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10])
y = npSigmoid(x)

plt.plot(x,y)
plt.show()