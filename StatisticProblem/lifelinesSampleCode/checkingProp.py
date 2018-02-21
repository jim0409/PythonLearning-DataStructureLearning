from matplotlib.pylab import plt
from lifelines.datasets import load_dd
from lifelines import KaplanMeierFitter

data = load_dd()

# checking proportional hazards assumption
# if the curves are parallel (and hence do not cross each other),
# then it's likely the variable satisfies the assumption.
# if the curves do cross, likely you'll have to "stratify" the variable

# In lifelines, the KaplanMeierFitter object has a .plot_loglogs function for this purpose

democracy_0 = data.loc[data['democracy'] == 'Non-democracy']
democracy_1 = data.loc[data['democracy'] == 'Democracy']

kmf0 = KaplanMeierFitter()
kmf0.fit(democracy_0['duration'], event_observed=democracy_0['observed'])

kmf1 = KaplanMeierFitter()
kmf1.fit(democracy_1['duration'], event_observed=democracy_1['observed'])

fig, axes = plt.subplots()
kmf0.plot_loglogs(ax=axes)
kmf1.plot_loglogs(ax=axes)

axes.legend(['Non-democracy', 'Democracy'])

plt.show()
