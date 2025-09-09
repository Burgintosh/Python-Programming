import numpy as np
from random import random
import matplotlib.pyplot as plt
from scipy.stats import linregress

## Lab 13: Monte Carlo Lab ##

_author_ = "Burgess Doan III"
_credits_ = ["https://numpy.org/doc/stable/reference/generated/numpy.count_nonzero.html"]
_email_ = "doanbs@mail.uc.edu"

# Formatted with Black Formatter
# https://pypi.org/project/black/

balls = np.arange(1, 1001)
non_empty_bins = []
for N in balls:
    bins = np.zeros(N)  # Initialize empty bins
    for b in range(N):
        bins[int(N * random())] += 1  # Increment the count of balls in the selected bin
    result = np.count_nonzero(bins != 0)
    non_empty_bins.append(result)
    print(f"Number of Balls: {N}, Non-Empty Bins: {result}")
    
slope, intercept, r_value, p_value, std_err = linregress(balls, non_empty_bins)
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-value: {r_value}")
plt.plot(balls, non_empty_bins)
plt.show()
