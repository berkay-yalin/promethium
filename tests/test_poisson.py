"""test the poisson distribution against the scipy library"""
import random
import scipy
from utility import compare_distributions
import promethium

def test_poisson_pmf():
    expected_function = scipy.stats.poisson.pmf
    observed_function = promethium.poisson.pmf
    for _ in range(1000):
        x = random.randint(0, 100)
        lambda_ = random.uniform(0, 100.0)
        compare_distributions(expected_function, observed_function, (x, lambda_))

def test_poisson_cdf():
    expected_function = scipy.stats.poisson.cdf
    observed_function = promethium.poisson.cdf
    for _ in range(1000):
        x = random.randint(0, 100)
        lambda_ = random.uniform(0, 100.0)
        compare_distributions(expected_function, observed_function, (x, lambda_))

def test_poisson_ppf():
    expected_function = scipy.stats.poisson.ppf
    observed_function = promethium.poisson.ppf
    for _ in range(100):
        y = random.uniform(0, 1.0)
        lambda_ = random.uniform(0, 100.0)
        compare_distributions(expected_function, observed_function, (y, lambda_))

if __name__ == '__main__':
    test_poisson_pmf()
    test_poisson_cdf()
    test_poisson_ppf()
