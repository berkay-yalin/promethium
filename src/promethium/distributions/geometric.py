from typing import Any, Union
from decimal import Decimal


def pmf_validate(x: Any, p: Any) -> None:
    if not isinstance(x, int):
        raise TypeError("x value must be a non-negative integer")
    if x < 0:
        raise ValueError("x value out of domain")
    if not isinstance(p, float):
        raise TypeError("p value must be non-negative float")
    if not 0 <= p <= 1:
        raise ValueError("p value out of domain")

def pmf_calculate(x: int, p: Decimal) -> Decimal:
    return ((1 - p) ** (x - 1)) * p

def pmf(x: int, p: Union[int, float]) -> Decimal:
    pmf_validate(x, p)

    if x == 0:
        return Decimal("0.0")

    return pmf_calculate(x, Decimal(str(p)))


def cdf_calculate(x: int, p: Decimal) -> Decimal:
    return 1 - (1 - p) ** x

def cdf(x: int, p: float) -> Decimal:
    pmf_validate(x, p)
    return cdf_calculate(x, Decimal(str(p)))


def ppf_validate(area: Any, p: Any) -> None:
    if not isinstance(area, float):
        raise TypeError("area value must be non-negative float")
    if not 0 <= area <= 1:
        raise ValueError("area value out of domain")
    if not isinstance(p, float):
        raise TypeError("p value must be non-negative float")
    if not 0 <= p <= 1:
        raise ValueError("p value out of domain")

def ppf_calculate(area: Decimal, p: Decimal) -> int:
    cumulative = Decimal()
    i = 1
    while cumulative <= area:
        cumulative += pmf_calculate(i, p)
        i += 1
    return i - 1

def ppf(area: float, p: float) -> int:
    ppf_validate(area, p)
    return ppf_calculate(
        Decimal(str(area)),
        Decimal(str(p))
    )


__all__ = ['pmf', 'cdf', 'ppf']

