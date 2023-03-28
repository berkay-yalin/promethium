from typing import Any, Union
from fractions import Fraction
import math


def PoissonPD_validate(k: Any, mu: Any) -> None:
	if not isinstance(k, int):
		raise TypeError("k value must be an integer")
	if not isinstance(mu, (int, float)):
		raise TypeError("λ data type unsupported")
	if mu < 0:
		raise ValueError("λ value out of domain")

def PoissonPD_calculate(k: int, mu: Fraction) -> float:
	return ((mu ** k) / math.factorial(k)) * (math.e ** -mu)

def PoissonPD(k: int, mu: Union[int, float]) -> float:
	PoissonPD_validate(k, mu)
	return PoissonPD_calculate(k, Fraction(str(mu)))


def PoissonCD_calculate(k: int, mu: Fraction) -> float:
	return sum([PoissonPD_calculate(i, mu) for i in range(k + 1)])

def PoissonCD(k: int, mu: Union[int, float]) -> float:
	PoissonPD_validate(k, mu)
	return PoissonCD_calculate(k, Fraction(str(mu)))


def InvPoissonCD_validate(area: Any, mu: Any) -> None:
	if not isinstance(area, (int, float)):
		raise TypeError("area data type unsupported")
	if not isinstance(mu, (int, float)):
		raise TypeError("λ data type unsupported")
	if not 0 <= mu <= 1:
		raise ValueError("λ value out of domain")

def InvPoissonCD_calculate(area: Fraction, mu: Fraction) -> int:
	cumulative = 0
	ppd = 0
	i = 0
	while cumulative <= area:
		ppd = PoissonPD_calculate(i, mu)
		cumulative += ppd
		i += 1

	return i - 1

def InvPoissonCD(area: Union[int, float], mu: Union[int, float]) -> int:
	InvPoissonCD_validate(area, mu)
	return InvPoissonCD_calculate(Fraction(str(area)), Fraction(str(mu)))
