from lifelines.datasets import load_rossi
from lifelines import CoxPHFitter

rossi_dataset = load_rossi()

# print((load_rossi().head()))

cph = CoxPHFitter()
cph.fit(rossi_dataset, duration_col='week', event_col='arrest')

cph.print_summary()  # access the results using cph.summary

# show coef of each hazard rate from coxph
# print(cph.hazards_)

# show hazard rate from each observation's variable
# print(cph.baseline_hazard_)

# Goodness of fit and prediction :want to know how “good” of a fit your model was to the data

# Method 1. See Concordance-index
# Model Selection in Survival Regression : http://lifelines.readthedocs.io/en/latest/Survival%20Regression.html#model-selection-in-survival-regression



# Method 2. Compare spread between the baseline survival function vs the Kaplan Meier survival function
# a small spread between these two curves means that the impact of the exponential in the Cox model does very little
# whereas a large spread means most of the changes in individual hazard can be attributed to the exponential term

