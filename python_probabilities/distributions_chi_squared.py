# https://statproofbook.github.io/P/chi2-pdf.html
from typing import Union, Any
import math
import scipy.special as sc
from scipy import stats

def Chi_squaredPD_validate(x: Any, df: Any) -> None:
	if not isinstance(x, (int, float)):
		raise TypeError("Input x value is invalid")
	if not isinstance(df, int):
		raise TypeError("Input df value is invalid")

def Chi_squaredPD_calculate(x: Any, df: Any) -> float:
	return (1/((2**(df/2))*math.gamma(df/2)))*(x**((df/2)-1))*math.exp(-x/2)

def Chi_squaredPD(x: Union[int, float], df: Union[int, float]) -> float:
	Chi_squaredPD_validate(x, df)
	return Chi_squaredPD_calculate(float(x), float(df))


def Chi_squaredCD_calculate(x: float, df: float) -> float:
	return sc.gammainc(df/2,x/2)

def Chi_squaredCD(x: Union[int, float], df: Union[int, float]) -> float:
	Chi_squaredPD_validate(x, df)
	return Chi_squaredCD_calculate(float(x), float(df))

def InvChi_squaredCD_validate(area: Any, df: Any) -> None:
	if not isinstance(area, float) or not 0 <= area <= 1:
		raise TypeError("Input area must be a float between 0 and 1")
	if not isinstance(df, int):
		raise TypeError("Input df value must be a positive integer")


def InvChi_squaredCD_calculate(area: float, df: int):
	return stats.chi2.isf(area,df)

def InvChi_squaredCD(area: Union[int, float], df: Union[int, float]) -> float:
	InvChi_squaredCD_validate(area, df)
	return InvChi_squaredCD_calculate(
		float(area),
		float(df),
	) #type:ignore
