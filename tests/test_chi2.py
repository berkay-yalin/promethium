"""test the chi2 distribution against the scipy library"""
import random
import scipy
from utility import compare_distributions
import promethium

def test_chi2_pdf():
    expected_function = scipy.stats.chi2.pdf
    observed_function = promethium.chi2.pdf
    for _ in range(1000):
        x = random.uniform(0, 1.0)
        df = random.randint(1, 100)
        compare_distributions(expected_function, observed_function, (x, df))

def test_chi2_cdf():
    expected_function = scipy.stats.chi2.cdf
    observed_function = promethium.chi2.cdf
    for _ in range(1000):
        x = random.uniform(0, 1.0)
        df = random.randint(1, 100)
        compare_distributions(expected_function, observed_function, (x, df))

if __name__ == '__main__':
    test_chi2_pdf()
    test_chi2_cdf()
