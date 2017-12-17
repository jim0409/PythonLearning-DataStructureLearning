from lifelines.plotting import plot_lifetimes
from numpy.random import uniform, exponential
import numpy as np
import matplotlib.pylab as plt

N = 25
current_time = 10
actual_lifetimes = np.array([[exponential(12), exponential(2)][uniform() < 0.5] for i in range(N)])
observed_lifetimes = np.minimum(actual_lifetimes, current_time)
observed = actual_lifetimes < current_time

plt.xlim(0, 25)
plt.vlines(10, 0, 30, lw=2, linestyles='--')
plt.xlabel("time")
plt.title("Births and deaths of our population, at $t=10$")
plot_lifetimes(observed_lifetimes, event_observed=observed)
print("Observed lifetimes at time %d:\n" % (current_time), observed_lifetimes)