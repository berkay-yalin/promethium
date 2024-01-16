from typing import Any, Union
from decimal import Decimal
from math import factorial


def pmf_validate(k: Any, lambda_: Any) -> None:
    if not isinstance(k, int):
        raise TypeError("k value lambda_st be an integer")
    if not isinstance(lambda_, (int, float)):
        raise TypeError("λ data type unsupported")
    if lambda_ <= 0:
        raise ValueError("λ value out of domain")

def pmf_calculate(k: int, lambda_: Decimal) -> Decimal:
    return (lambda_ ** k) / ( factorial(k) * lambda_.exp() )

def pmf(k: int, lambda_: Union[int, float]) -> float:
    pmf_validate(k, lambda_)
    return float(pmf_calculate(k, Decimal(str(lambda_))))


def cdf_calculate(k_upper: int, lambda_: Decimal, k_lower: int = 0) -> Decimal:
    return sum((pmf_calculate(i, lambda_) for i in range(k_lower, k_upper + 1)), Decimal())

def cdf(k: int, lambda_: Union[int, float]) -> float:
    pmf_validate(k, lambda_)
    return float(cdf_calculate(k, Decimal(str(lambda_))))


def ppf_validate(area: Any, lambda_: Any) -> None:
    if not isinstance(area, (int, float)):
        raise TypeError("area data type unsupported")
    if area < 0:
        raise ValueError("area value out of domain")
    if not isinstance(lambda_, (int, float)):
        raise TypeError("λ data type unsupported")
    if lambda_ <= 0:
        raise ValueError("λ value out of domain")

def ppf_calculate(area: Decimal, lambda_: Decimal) -> int:
    tempK: int = 0
    while True:
        if cdf_calculate(tempK, lambda_) >= area:
            break
        tempK += 1
    return tempK

def ppf(area: Union[int, float], lambda_: Union[int, float]) -> int:
    ppf_validate(area, lambda_)
    return ppf_calculate(Decimal(str(area)), Decimal(str(lambda_)))

__all__ = ['pmf', 'cdf', 'ppf']

