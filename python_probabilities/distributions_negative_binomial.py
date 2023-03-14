from decimal import Decimal
import math

def NegativeBinomialPD(xInput: int, rInput: int, pInput: float) -> Decimal:
	NegativeBinomialPD_validate(xInput, rInput, pInput)
	return NegativeBinomialPD_calculate(xInput, rInput, Decimal(str(pInput)))

def NegativeBinomialPD_validate(x: object, r: object, p: object) -> None:
	if not isinstance(x, int) or x < 0:
		raise TypeError("Input value x must be positive integer")
	if not isinstance(r, int) or r < 0:
		raise TypeError("Input value n must be positive integer")
	if r > x:
		raise TypeError("Number of successes must be less than trials")
	if not isinstance(p, float) or not 0 <= p <= 1:
		raise TypeError("Input value p must be a positive decimal percentage")

def NegativeBinomialPD_calculate(x: int, r: int, p: Decimal) -> Decimal:
	return math.comb(x-1, r-1) * (p**r) * ((1-p) ** (x-r))


def NegativeBinomialCD(xInput: int, rInput: int, pInput: float) -> Decimal:
	NegativeBinomialPD_validate(xInput, rInput, pInput)
	return NegativeBinomialCD_calculate(xInput, rInput, pInput)

def NegativeBinomialCD_calculate(x: int, r: int, p: Decimal):
	return sum([NegativeBinomialPD(i, r, p) for i in range(r, x+1)])


def InvNegativeBinomialCD():
	pass

def InvNegativeBinomialCD_validate():
	pass

def InvNegativeBinomialCD_calculate():
	pass