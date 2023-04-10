from typing import Any, Union
from decimal import Decimal

def GeometricPD(x: int, p: Union[int, float]) -> Decimal:
    GeometricPD_validate(x, p)
    return GeometricPD_calculate(x, Decimal(str(p)))

def GeometricPD_validate(x: Any, p: Any) -> None:
    if not isinstance(x, int):
        raise TypeError("x value must be a non-negative integer")
    if x < 0:
        raise ValueError("x value out of domain")
    if not isinstance(p, float):
        raise TypeError("p value must be non-negative float")
    if not 0 <= p <= 1:
        raise ValueError("p value out of domain")

def GeometricPD_calculate(x: int, p: Decimal) -> Decimal:
    return ((1 - p) ** (x - 1)) * p


def GeometricCD(x: int, p: float) -> Decimal:
    GeometricPD_validate(x, p)
    return GeometricCD_calculate(x, Decimal(str(p)))

def GeometricCD_calculate(x: int, p: Decimal) -> Decimal:
    return 1 - (1 - p) ** x


def InvGeometricCD(area: float, p: float) -> int:
    InvGeometricCD_validate(area, p)
    return InvGeometricCD_calculate(
        Decimal(str(area)),
        Decimal(str(p))
    )

def InvGeometricCD_validate(area: Any, p: Any) -> None:
    if not isinstance(area, float):
        raise TypeError("area value must be non-negative float")
    if not 0 <= area <= 1:
        raise ValueError("area value out of domain")
    if not isinstance(p, float):
        raise TypeError("p value must be non-negative float")
    if not 0 <= p <= 1:
        raise ValueError("p value out of domain")

def InvGeometricCD_calculate(area: Decimal, p: Decimal) -> int:
    cumulative = Decimal()
    i = 1
    while cumulative <= area:
        cumulative += GeometricPD_calculate(i, p)
        i += 1
    return i - 1

