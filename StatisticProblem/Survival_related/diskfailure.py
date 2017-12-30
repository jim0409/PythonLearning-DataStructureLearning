import pandas as pd
import lifelines
import matplotlib.pylab as plt
from lifelines import KaplanMeierFitter

data = pd.read_table('../csv-folder/data1.csv',sep=',')
T = data['smart_9_raw']
E = data['failure']

kmf = KaplanMeierFitter()
kmf.fit(T,event_observed=E)
kmf.survival_function_.plot()

plt.show()



