from typing import Any
from decimal import Decimal
from math import comb


def pmf_validate(x: Any, n: Any, p: Any) -> None:
    if not isinstance(x, int):
        raise TypeError("x must be a non-negative integer")
    if x < 0:
        raise ValueError("x value out of domain")
    if not isinstance(n, int):
        raise TypeError("n must be a non-negative integer")
    if n < 0:
        raise ValueError("n value out of domain")
    if not isinstance(p, float):
        raise TypeError("p must be non-negative float")
    if not 0 <= p <= 1:
        raise ValueError("p value out of domain")

def pmf_calculate(x: int, n: int, p: Decimal) -> Decimal:
    return comb(n, x) * (p ** x) * ((1 - p) ** (n - x))

def pmf(x: int, n: int, p: float) -> Decimal:
    pmf_validate(x, n, p)
    return pmf_calculate(x, n, Decimal(str(p)))


def cdf_calculate(k_upper: int, n: int, p: Decimal, k_lower: int = 0) -> Decimal:
    return sum((pmf_calculate(i, n, p) for i in range(k_lower, k_upper + 1)), Decimal())

def cdf(x: int, n: int, p: float) -> Decimal:
    pmf_validate(x, n, p)
    return cdf_calculate(x, n, Decimal(str(p)))


def ppf_validate(y: Any, n: Any, p: Any) -> None:
    if not isinstance(y, float):
        raise TypeError("y must be non-negative float")
    if not 0 <= y <= 1:
        raise ValueError("y value out of domain")
    if not isinstance(n, int):
        raise TypeError("n must be a non-negative integer")
    if n < 0:
        raise ValueError("n value out of domain")
    if not isinstance(p, float):
        raise TypeError("p must be non-negative float")
    if not 0 <= p <= 1:
        raise ValueError("p value out of domain")

def ppf_calculate(x: Decimal, n: int, p: Decimal) -> int:
    tempN = -1
    for i in range(n + 1):
        tempX = cdf_calculate(tempN, n, p)
        if tempX >= x:
            return tempN
        tempN = i
    return n


def ppf(y: float, n: int, p: float) -> int:
    ppf_validate(y, n, p)
    return ppf_calculate(Decimal(str(y)), n, Decimal(str(p)))


__all__ = ['pmf', 'cdf', 'ppf']

