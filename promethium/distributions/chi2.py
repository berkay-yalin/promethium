from typing import Union, Any
from decimal import Decimal
from math import gamma
from ..special.gamma import gammainc


HALF = Decimal('0.5')
TWO = Decimal('2')


def pdf_validate(x: Any, df: Any) -> None:
    if not isinstance(x, (int, float)):
        raise TypeError("Input x value is invalid")
    if not isinstance(df, int):
        raise TypeError("Input df value is invalid")
    if df <= 0:
        raise ValueError("df value out of domain")

def pdf_calculate(x: Decimal, df: Decimal) -> Decimal:
    df_half = df * HALF
    return (
        ( x ** (df_half - 1) * (-x * HALF).exp() )
        / ( TWO ** df_half * Decimal(f"{gamma(df_half)}") )
    )

def pdf(x: Union[int, float], df: int) -> Decimal:
    pdf_validate(x, df)
    return pdf_calculate(
        Decimal(str(x)),
        Decimal(str(df))
    )


def cdf(x: Union[int, float], df: int) -> float:
    pdf_validate(x, df)
    return gammainc(x * 0.5, df * 0.5)


__all__ = ['pdf', 'cdf']

