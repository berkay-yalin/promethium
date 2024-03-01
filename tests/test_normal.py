"""test the normal distribution against the scipy library"""
import random
import scipy
from utility import compare_distributions
import promethium

def test_normal_pdf():
    expected_function = scipy.stats.norm.pdf
    observed_function = promethium.normal.pdf
    for _ in range(1000):
        x = random.randint(0, 100)
        mu = random.uniform(0, 100.0)
        sigma = random.uniform(0, 100.0)
        compare_distributions(expected_function, observed_function, (x, mu, sigma))

def test_normal_cdf():
    expected_function = scipy.stats.norm.cdf
    observed_function = promethium.normal.cdf
    for _ in range(1000):
        x = random.randint(0, 100)
        mu = random.uniform(0, 100.0)
        sigma = random.uniform(0, 100.0)
        compare_distributions(expected_function, observed_function, (x, mu, sigma))

def test_normal_ppf():
    expected_function = scipy.stats.geom.pmf
    observed_function = promethium.geometric.pmf
    for _ in range(1000):
        x = random.randint(0, 100)
        p = random.uniform(0, 1.0)
        compare_distributions(expected_function, observed_function, (x, p))

if __name__ == '__main__':
    test_normal_pdf()
    test_normal_cdf()
    test_normal_ppf()
