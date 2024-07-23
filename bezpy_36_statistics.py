# TRY  https://towardsdatascience.com/the-statistical-greek-alphabet-in-python-65295526146
# TRY https://towardsdatascience.com/an-introduction-to-linear-regression-for-data-science-9056bbcdf675
# TRY https://towardsdatascience.com/altair-statistical-visualization-library-for-python-cfb63847c0c0
# TRY https://towardsdatascience.com/how-to-use-simulations-for-hypothesis-tests-6f0ac53a9c8f
# TRY https://towardsdatascience.com/how-to-successfully-run-a-b-tests-f3ca363dec98

import random as rand
import numpy as np
import scipy.stats as scs
from statistics import *           # Standard Library
from math import sqrt
from sympy import init_printing, var, latex, exp   # note sympy is used for algebraic expressions, it is a computer algebra system (CAS)
from IPython.display import *
init_printing(use_latex=True)
import matplotlib.pyplot as plt
# import statsmodels   --- have a look at this

def degreesOfFreedom(X, Y):
    s1 = (stdev(X)**2)
    s2 = (stdev(Y)**2)
    df = (s1 / len(X) + s2 / len(Y))**2 / ((s1 / len(X))**2 / (len(X) - 1) + (s2 /  len(Y))**2 / len(Y) - 1)
    return(df)




# Standard Library  'statistics'. see https://www.w3schools.com/python/module_statistics.asp


#=======================================================================================================================
# Measures of Central Tendency
#=======================================================================================================================
# mean()            - Arithmetic mean (“average”) of data.
# fmean()           - floating point arithmetic mean, Faster than mean(), always returns float.  New in version 3.8.
# geometric_mean()  - Geometric mean of data.
# harmonic_mean()   - Harmonic mean of data.
# median()          - Median (middle value) of data.  Data doesn't need to be sorted
# median_low()      - Low median of data. Will not return arithmetic mean of central two values but the lowest one
# median_high()     - High median of data. Will not return arithmetic mean of central two values but the highest one
# median_grouped()  - Median, or 50th percentile, of grouped data. Default interval  = 1
# mode()            - Single mode (most common value) of discrete or nominal data.
# multimode()       - List of modes (most common values) of discrete or nominal (categorical) data.
# quantiles()       - Divide data into intervals with equal probability.  (Version 3.8)
# StatisticsError   - Subclass of ValueError for statistics-related exceptions.


#=======================================================================================================================
# Measures of Spread
#=======================================================================================================================
# pstdev()      # Population standard deviation of data.
# pvariance()   # Population variance of data.
# stdev()       # Sample standard deviation of data.
# variance()    # Sample variance of data.



if __name__ == '__main__':

    mean([1, 2, 3])                 # 2
    fmean([1, 2, 3, 4, 4])          # 2.8
    harmonic_mean([40, 60, 80])     # 55.38...
    median([1, 3, 5, 7])            # 4.0
    median_low([1, 3, 5, 7])        # 3
    median_high([1, 3, 5, 7])       # 5
    mode([1, 1, 2, 3, 3, 3, 3, 4])  # 3
    mode(['red', 'green', 'blue', 'red'])  # red
    mode('aabbbbccddddeeffffgg')           # returns the first mode 'b'
    multimode('aabbbbccddddeeffffgg')      # Returns list of most frequent values  ['b', 'd', 'f']

    # ==================================================================================================================
    # median_grouped(data, interval=1) for continuous data
    # ==================================================================================================================
    # The common method is as follows ...
    # 1) Order the data set provided in the categorized groups
    # 2) Find the median interval which is the median range using specified interval width (default is 1)
    # 3) interpolate within that range using the formula ...
    #   grouped_median = L + interval * (N/2 - CF)/F.
    #       L = lower limit of the median interval
    #       N = total number of data points
    #       CF = number of data points below the median interval (PYTHON = number of points below the median value)
    #       F = number of data points in the median interval (PYTHON = number of points below the median value)
    # The actual values of each data point is irrelevant, each data point is considered the midpoint of their interval
    # It is assumed that the true values within that interval are distributed uniformly
    # WARNING: However python's function uses a similar algorigthm (see _median_grouped())

    data = (10, 12, 13, 12, 13, 15)   # which sorts to [10, 12, 12, 13, 13, 15]
    median_grouped(data)  # grouped as  [9.5-10.5)x1, [12.5-13.5)x4, [14.5-15.5)x1 --> returns 12.5
    median_grouped(data, 2)  # grouped as  [10-12)x1, [12-14)x4, [14-16)x1 --> returns 12.5
    median_grouped(data, 5)  # grouped as  [0.5-5.5) x0, [5.5-10.5) x1, [10.5-15.5) x4 --> returns 12.5
    median_grouped([45.0, 55.0, 65.0, 75.0, 85.0], interval=10)  # Each datapoint is the middle point of the group interval

    def _find_lteq(data, x):
        return data.index(x)

    def _find_rteq(data, x):
        data.reverse()
        return len(data) - data.index(x) - 1

    def _median_grouped(data, interval):
        data = sorted(data)
        print(f'data={data}')
        n = len(data)  # Number of points
        x = data[n // 2]  # Value at the midpoint (centre of the interval)
        L = x - interval / 2  # Lower limit of the median interval
        l1 = _find_lteq(data, x)  # Position of leftmost occurrence of x in data
        l2 = _find_rteq(data, x)  # Position of righmost occurrence of x in data
        cf = l1                   # Number of points before the first occurrance of x
        f = l2 - l1 + 1  # Number of occurrences of x
        grouped_median =  L + interval * (n / 2 - cf) / f  # Interpolation

        print(f'data_points={n}')
        print(f'median_value={x}')
        print(f'lower limit of median interval={L}')
        print(f'upper limit of median interval={x + interval/2}')
        print(f'index of first median value={l1}')
        print(f'index of first median value={l2}')
        print(f'points before median value={cf}')
        print(f'occurrences of median value={f}')
        print(f'grouped_median={grouped_median}')
        return grouped_median

    data = [5] * 2 + [15] * 4 + [25] * 5 + [35]* 4  + [45] * 2
    _median_grouped(data, 5)

    data = [5] * 7 + [15] * 10 + [25] * 23 + [35]* 51  + [45] * 6 + [55] * 3
    _median_grouped(data, 10)
    # ==================================================================================================================

    data = [0.0, 0.25, 0.75, 1.25, 1.75, 2.00, 2.75, 3.25]   # does not need to be ordered
    mu = mean(data)  # 1.375
    md = median(data)
    population_sd = pstdev(data)           # Population sd
    population_var = pvariance(data)       # Population var
    population_var2 = pvariance(data, mu)  # Quicker than above, as the mean is already calculated and passed as a parameter
    sample_sd = stdev(data)                # Sample sd
    sample_var = variance(data)            # Sample variance

    # ================================================================
    # quantiles are new in version 3.8. to determine class boundaries
    # ================================================================
    # n=4 for quartiles (default)  method='exclusive' (default)
    # The cut points are linearly interpolated from the two nearest data points. For example, if a cut point falls
    # one-third of the distance between two sample values, 100 and 112, the cut-point will evaluate to 104.
    # “inclusive” is used for describing population data or for samples that are known to include the most extreme values from the population
    # “exclusive”  is used for data sampled from a population that can have more extreme values than found in the samples

    data = list(range(1,10))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

    min_value = min(data)
    max_value = max(data)

    qt1 = quantiles(data, n=4, method='exclusive')   # [2.5, 5.0, 7.5]
    qt2 = quantiles(data, n=4, method='inclusive')   # [3.0, 5.0, 7.0]



    data = [55, 75, 75, 79, 81,
            84, 84, 86, 86, 86,
            87, 87, 87, 88, 89,
            90, 91, 92, 95, 99,
            100, 101, 101, 101, 101,
            103, 103, 103, 103, 103,
            104, 105, 105, 106, 106,
            107, 107, 108, 109, 109,
            110, 111, 111, 111, 111,
            112, 119, 121, 129, 145]

    deciles = quantiles(data, n=10) # method='exclusive'  # [81.3, 86.2, 89.3, 99.4, 102.0, 103.6, 106.7, 109.8, 111.9]
    deciles = quantiles(data, n=10, method='inclusive')   # [83.7, 86.8, 89.7, 99.6, 102.0, 103.4, 106.3, 109.2, 111.1]

    # ================================================================
    # Normal Distribution
    # ================================================================
    x = NormalDist(mu=10.0, sigma=2.0)  # Returns a new NormalDist object  (Version 3.9)

    values = x.mean, x.median, x.mode, x.stdev, x.variance  # Read Only Values
   # z_score = x.zscore(12)
    probability_df = x.pdf(10)
    cumulative_df = x.cdf(10)   # Returns P(X <= x)
    inv_cdf = x.inv_cdf(0.95)   # Returns x: P(X <= x) = 0.95

    x.samples(10)  # Generate sample list of 10 values in the distribution
    x.samples(10, seed=874664)  # Use a specific seed to allow for a repeatable data sample

    x.quantiles(n=4)  # Divides distribution into quantiles  (see above)

    x = NormalDist(-3, 1)
    y = NormalDist(3, 1)
    x.overlap(y)  # Returns the overlap area for the two distributions


    # ================================================================
    # Display Normal Distribution
    # ================================================================
    fig = plt.gcf()  # Get the current figure
    fig.set_size_inches(8,5)
    var('x')
    f = lambda x: exp(-x**2/2)
    display(Latex('$ \large f(x) = ' + latex(f(x)) + '$'))
    x = np.linspace(-4,4,100)
    y = np.array([f(v) for v in x],dtype='float')
    plt.grid(True)
    plt.title('The Normal Distribution')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.plot(x,y,color='gray')
    plt.fill_between(x,y,0,color='#c0f0c0')
    plt.show()

    population = data = [5, 10, 15, 20, 19, 29, 5, 33, 29, 17, 17, 18, 12, 29, 26]
    length_of_sample = 5 # <- Also known as n
    sample = rand.sample(data, length_of_sample)

    # Length of Sample / Population
    n = len(sample)
    N = len(data)


    sample_mean = np.mean(sample) # x-bar
    sigma = sum(data)
    pop_mean = sigma / N        # population mean 'mu'
    sample_median = np.median(sample)



    # Correlation Coefficient (Pearson)
    a = [1,2,3,4]
    b = [2,4,6,8]
    r = scs.pearsonr(a,b)

    # Standard Deviation
    var = variance(sample)
    pop_var = pvariance(data)
    sdev = stdev(sample)
    pop_sdev = pstdev(data)

    # Proportion
    p_hat = N / n
    p = n / N

    # Standard Error of the Mean
    se = scs.sem(sample) / sqrt(n) # Sigma-X-Bar

    # Standard Error of the Proportion
    sep = sqrt(p*(1 - p) / n)

    # Chi-Squared
    chi_sq = scs.chi2(data)
