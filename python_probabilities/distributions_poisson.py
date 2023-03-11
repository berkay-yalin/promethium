from fractions import Fraction
import math


def PoissonPD_validate(k: object, p: object) -> None:
	if not isinstance(k, int):
		raise TypeError("Input value k must be integer")
	if not isinstance(p, (int, float)):
		raise TypeError("Input value p is invalid")
	if p <= 0:
		raise ValueError("Input value p out of domain")

def PoissonPD_calculate(k: int, p: Fraction) -> float:
	return ((p ** k) / math.factorial(k)) * (math.e ** -p)

def PoissonPD(kInput: int, pInput: float) -> float:
	PoissonPD_validate(kInput, pInput)
	return PoissonPD_calculate(kInput, Fraction(str(pInput)))


def PoissonCD_calculate(k: int, p: Fraction) -> float:
	return sum([PoissonPD_calculate(i, p) for i in range(k + 1)])

def PoissonCD(kInput: int, pInput: float) -> float:
	PoissonPD_validate(kInput, pInput)
	return PoissonCD_calculate(kInput, Fraction(str(pInput)))


def InvPoissonCD_validate(area: object, l: object):
	if not isinstance(area, float):
		raise TypeError("Input value area must be float")
	if not isinstance(l, (int, float)):
		raise TypeError("Input value l must be float")
	if area < 0 or area > 1:
		raise ValueError("Input value area out of domain")

def InvPoissonCD_calculate(area: Fraction, l: Fraction):
	cumulative = 0
	ppd = 0
	i = 0
	while cumulative <= area:
		ppd = PoissonPD_calculate(i, l)
		cumulative += ppd
		i += 1

	return i - 1

def InvPoissonCD(area: float, l: float):
	InvPoissonCD_validate(area, l)
	return InvPoissonCD_calculate(Fraction(str(area)), Fraction(str(l)))

