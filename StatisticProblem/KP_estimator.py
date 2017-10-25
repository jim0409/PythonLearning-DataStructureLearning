# https://lifelines.readthedocs.io/en/latest/Quickstart.html#kaplan-meier-and-nelson-aalen

import matplotlib.pylab as plt
import lifelines

data = lifelines.datasets.load_dd()

from lifelines import KaplanMeierFitter
kmf = KaplanMeierFitter()
T = data["duration"]
E = data["observed"]

kmf.fit(T, event_observed=E)
kmf.survival_function_.plot()
plt.title('Survival function of political regimes')

plt.show()

# KaplanMeierFitter.fit(durations, event_observed=None,
#                       timeline=None, entry=None, label='KM_estimate',
#                       alpha=None, left_censorship=False, ci_labels=None)
#
# Parameters:
# duration: an array, or pd.Series, of length n -- duration subject was observed for
#     timeline: return the best estimate at the values in timelines (postively increasing)
# event_observed: an array, or pd.Series, of length n -- True if the the death was observed, False if the event
# was lost (right-censored). Defaults all True if event_observed==None
# entry: an array, or pd.Series, of length n -- relative time when a subject entered the study. This is
# useful for left-truncated (not left-censored) observations. If None, all members of the population
# were born at time 0.
# label: a string to name the column of the estimate.
# alpha: the alpha value in the confidence intervals. Overrides the initializing
# alpha for this call to fit only.
# left_censorship: True if durations and event_observed refer to left censorship events. Default False
# ci_labels: add custom column names to the generated confidence intervals
# as a length-2 list: [<lower-bound name>, <upper-bound name>]. Default: <label>_lower_<alpha>
#
#
# Returns:
# a modified self, with new properties like 'survival_function_'.