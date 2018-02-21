from matplotlib.pylab import plt
from lifelines.datasets import load_rossi
from lifelines import CoxPHFitter

rossi_dataset = load_rossi()

cph = CoxPHFitter()

# stratification
cph.fit(rossi_dataset, 'week', event_col='arrest', strata=['race'])

cph.print_summary()  # access the results using cph.summary