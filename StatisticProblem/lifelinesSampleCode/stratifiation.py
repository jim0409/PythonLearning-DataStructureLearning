
# stratification
cph.fit(rossi_dataset, 'week', event_col='arrest', strata=['race'])

cph.print_summary()  # access the results using cph.summary