from lifelines.datasets import load_waltons
import matplotlib.pyplot as plt
df = load_waltons() # returns a Pandas DataFrame

# print(df.head())
# """
#     T  E    group
# 0   6  1  miR-137
# 1  13  1  miR-137
# 2  13  1  miR-137
# 3  13  1  miR-137
# 4  19  1  miR-137
# """
T = df['T']
E = df['E']

print(df)

from lifelines import KaplanMeierFitter
kmf = KaplanMeierFitter()
# 使用在kmf下的fit method可以做KP estimator
kmf.fit(T, event_observed=E)  # or, more succiently, kmf.fit(T, E)

# 使用survival_function_ 算出S(x)
# kmf.survival_function_
# 使用median_可以算出median survival time
# kmf.median_
# kmf.plot()

# 考慮multiple groups的情況
groups = df['group']
ix = (groups == 'miR-137')

kmf.fit(T[~ix], E[~ix], label='control')
ax = kmf.plot()

kmf.fit(T[ix], E[ix], label='miR-137')
kmf.plot(ax=ax)

plt.show()
