from typing import Any, Union
from decimal import Decimal
from math import factorial


def PoissonPD_validate(k: Any, lambda_: Any) -> None:
    if not isinstance(k, int):
        raise TypeError("k value lambda_st be an integer")
    if not isinstance(lambda_, (int, float)):
        raise TypeError("λ data type unsupported")
    if lambda_ <= 0:
        raise ValueError("λ value out of domain")

def PoissonPD_calculate(k: int, lambda_: Decimal) -> Decimal:
    return (lambda_ ** k) / ( factorial(k) * lambda_.exp() )

def PoissonPD(k: int, lambda_: Union[int, float]) -> float:
    PoissonPD_validate(k, lambda_)
    return float(PoissonPD_calculate(k, Decimal(str(lambda_))))


def PoissonCD_calculate(k: int, lambda_: Decimal) -> Decimal:
    return sum((PoissonPD_calculate(i, lambda_) for i in range(k + 1)), Decimal())

def PoissonCD(k: int, lambda_: Union[int, float]) -> float:
    PoissonPD_validate(k, lambda_)
    return float(PoissonCD_calculate(k, Decimal(str(lambda_))))


def InvPoissonCD_validate(area: Any, lambda_: Any) -> None:
    if not isinstance(area, (int, float)):
        raise TypeError("area data type unsupported")
    if area < 0:
        raise ValueError("area value out of domain")
    if not isinstance(lambda_, (int, float)):
        raise TypeError("λ data type unsupported")
    if lambda_ <= 0:
        raise ValueError("λ value out of domain")

def InvPoissonCD_calculate(area: Decimal, lambda_: Decimal) -> int:
    tempK: int = 0
    while True:
        if PoissonCD_calculate(tempK, lambda_) >= area:
            break
        tempK += 1
    return tempK

def InvPoissonCD(area: Union[int, float], lambda_: Union[int, float]) -> int:
    InvPoissonCD_validate(area, lambda_)
    return InvPoissonCD_calculate(Decimal(str(area)), Decimal(str(lambda_)))

