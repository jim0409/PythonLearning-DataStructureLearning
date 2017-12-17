from lifelines.statistics import logrank_test
import numpy as np

# define lifetimes A and B for comparison
lifetimes_A = np.random.exponential(3, size=500)
lifetimes_B = np.random.exponential(3, size=500)

results =logrank_test(lifetimes_A, lifetimes_B, alpha=0.95)

print(results.print_summary)

print("p_value:",results.p_value)
print("test_static:",results.test_statistic)
print("is_significant:",results.is_significant)