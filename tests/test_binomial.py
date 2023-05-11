from binomial import cdf_calculate as cdf_bin
from poisson import cdf_calculate as cdf_poiss

def test_cdf_bin():
     assert cdf_bin(10, 10, 0.5, 0) == 1

def test_cdf_poiss():
     assert cdf_poiss(10, 10, 0.5, 0) == 1