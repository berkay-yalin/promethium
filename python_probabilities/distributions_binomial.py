from typing import Any
from decimal import Decimal
from math import comb

def BinomialPD_validate(x: Any, n: Any, p: Any) -> None:
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

def BinomialPD_calculate(x: int, n: int, p: Decimal) -> Decimal:
    return comb(n, x) * (p ** x) * ((1 - p) ** (n - x))

def BinomialPD(x: int, n: int, p: float) -> Decimal:
    BinomialPD_validate(x, n, p)
    return BinomialPD_calculate(x, n, Decimal(str(p)))


def BinomialCD_calculate(k: int, n: int, p: Decimal) -> Decimal:
    return sum((BinomialPD_calculate(i, n, p) for i in range(k + 1)), Decimal())

def BinomialCD(x: int, n: int, p: float) -> Decimal:
    BinomialPD_validate(x, n, p)
    return BinomialCD_calculate(x, n, Decimal(str(p)))


def InvBinomialCD_validate(y: Any, n: Any, p: Any) -> None:
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

def InvBinomialCD_calculate(x: Decimal, n: int, p: Decimal) -> int:
    for i in range(n + 1):
        tempN = i - 1
        tempX = BinomialCD_calculate(tempN, n, p)
        if tempX == x:
            return i
        if tempX > x:
            return tempN

def InvBinomialCD(y: float, n: int, p: float) -> int:
    InvBinomialCD_validate(y, n, p)
    return InvBinomialCD_calculate(Decimal(str(y)), n, Decimal(str(p)))

