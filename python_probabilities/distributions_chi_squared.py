# https://statproofbook.github.io/P/chi2-pdf.html
from typing import Union, Any
import math
import scipy.special as sc
from scipy import stats

def ChiSquaredPD_validate(x: Any, df: Any) -> None:
    if not isinstance(x, (int, float)):
        raise TypeError("Input x value is invalid")
    if not isinstance(df, int):
        raise TypeError("Input df value is invalid")

def ChiSquaredPD_calculate(x: Any, df: Any) -> float:
    return (1/((2**(df/2))*math.gamma(df/2)))*(x**((df/2)-1))*math.exp(-x/2)

def ChiSquaredPD(x: Union[int, float], df: Union[int, float]) -> float:
    ChiSquaredPD_validate(x, df)
    return ChiSquaredPD_calculate(float(x), float(df))


def ChiSquaredCD_calculate(x: float, df: float) -> float:
    return sc.gammainc(df/2,x/2)

def ChiSquaredCD(x: Union[int, float], df: Union[int, float]) -> float:
    ChiSquaredPD_validate(x, df)
    return ChiSquaredCD_calculate(float(x), float(df))

def InvChiSquaredCD_validate(area: Any, df: Any) -> None:
    if not isinstance(area, float) or not 0 <= area <= 1:
        raise TypeError("Input area must be a float between 0 and 1")
    if not isinstance(df, int):
        raise TypeError("Input df value must be a positive integer")


def InvChiSquaredCD_calculate(area: float, df: int):
    return stats.chi2.isf(area,df)

def InvChiSquaredCD(area: Union[int, float], df: Union[int, float]) -> float:
    InvChiSquaredCD_validate(area, df)
    return InvChiSquaredCD_calculate(
        float(area),
        float(df),
    ) #type:ignore
