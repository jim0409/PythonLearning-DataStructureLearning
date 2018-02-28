# Quickstart
# http://lifelines.readthedocs.io/en/latest/Quickstart.html#installation

from lifelines.utils import datetimes_to_durations
from lifelines.utils import survival_table_from_events

# T, E = datetimes_to_durations(start_times, end_times, freq='h')
# table = survival_table_from_events(T, E)
# print(table.head())

"""
          removed  observed  censored  entrance  at_risk
event_at
0               0         0         0       163      163
6               1         1         0         0      163
7               2         1         1         0      162
9               3         3         0         0      160
13              3         3         0         0      157
"""
# start_times is a vector of datetime objects
# end_times is a vector of (possibly missing) datetime objects.

import numpy as np

# traditional way to gen survival time
# gen xS fro survival time and xC for censor time
# compare two of them if xS < xC implies that event happen else not
xS = np.random.exponential(1,10)
xC = np.random.exponential(1,10)
obsE = xS<xC

obsT = []
for i in range(0,10):
    if obsE[i]:
        obsT.append(xS[i])
    else :
        obsT.append(xC[i])

table = survival_table_from_events(obsT,obsE)
print(table.head())