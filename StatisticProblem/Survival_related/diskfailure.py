import pandas as pd
import lifelines
import matplotlib.pylab as plt
from lifelines import KaplanMeierFitter

data = pd.read_table('/home/ubuntu/Desktop/backblaze/2017-01-01.csv',sep=',')
T = data['smart_9_raw']
E = data['failure']

kmf = KaplanMeierFitter()
kmf.fit(T,event_observed=E)
kmf.survival_function_.plot()

plt.show()



