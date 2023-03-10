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



def PoissonCD_validate():
    pass

def PoissonCD_calculate():
    pass

def PoissonCD():
    pass



def InvPoissonCD_validate():
    pass

def InvPoissonCD_calculate():
    pass

def InvPoissonCD():
    pass
