"""test the geometric distribution against the scipy library"""
import random
import scipy
from utility import compare_distributions
import promethium

def test_geometric_pmf():
    expected_function = scipy.stats.geom.pmf
    observed_function = promethium.geometric.pmf
    for _ in range(1000):
        x = random.randint(0, 100)
        p = random.uniform(0.001, 1.0)
        compare_distributions(expected_function, observed_function, (x, p))

def test_geometric_cdf():
    expected_function = scipy.stats.geom.cdf
    observed_function = promethium.geometric.cdf
    for _ in range(1000):
        x = random.randint(0, 100)
        p = random.uniform(0.001, 1.0)
        compare_distributions(expected_function, observed_function, (x, p))

def test_geometric_ppf():
    expected_function = scipy.stats.geom.ppf
    observed_function = promethium.geometric.ppf
    for _ in range(1000):
        y = random.uniform(0, 0.999)
        p = random.uniform(0.001, 1.0)
        compare_distributions(expected_function, observed_function, (y, p))

if __name__ == '__main__':
    test_geometric_pmf()
    test_geometric_cdf()
    test_geometric_ppf()
