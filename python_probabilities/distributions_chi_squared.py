from typing import Union, Any
from decimal import Decimal
from math import gamma

from .special.gamma import gammainc

HALF = Decimal('0.5')
TWO = Decimal('2')

def ChiSquaredPD_validate(x: Any, df: Any) -> None:
    if not isinstance(x, (int, float)):
        raise TypeError("Input x value is invalid")
    if not isinstance(df, int):
        raise TypeError("Input df value is invalid")
    if df <= 0:
        raise ValueError("df value out of domain")

def ChiSquaredPD_calculate(x: Decimal, df: Decimal) -> Decimal:
    df_half = df * HALF
    return (
        ( x ** (df_half - 1) * (-x * HALF).exp() )
        / ( TWO ** df_half * Decimal(f"{gamma(df_half)}") )
    )

def ChiSquaredPD(x: Union[int, float], df: int) -> Decimal:
    ChiSquaredPD_validate(x, df)
    return ChiSquaredPD_calculate(
        Decimal(str(x)),
        Decimal(str(df))
    )

def ChiSquaredCD(x: Union[int, float], df: int) -> float:
    ChiSquaredPD_validate(x, df)
    return gammainc(x * 0.5, df * 0.5)

# def InvChiSquaredCD_validate(area: Any, df: Any) -> None:
#     if not isinstance(area, float) or not 0 <= area <= 1:
#         raise TypeError("Input area must be a float between 0 and 1")
#     if not isinstance(df, int):
#         raise TypeError("Input df value must be a positive integer")
#
# def InvChiSquaredCD_calculate(area: float, df: int):
#     return stats.chi2.isf(area,df)
#
# def InvChiSquaredCD(area: Union[int, float], df: Union[int, float]) -> float:
#     InvChiSquaredCD_validate(area, df)
#     return InvChiSquaredCD_calculate(
#         float(area),
#         float(df),
#     )

