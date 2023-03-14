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

def NegativeBinomialCD_calculate(x: int, r: int, p: Decimal) -> Decimal:
	return sum([NegativeBinomialPD(i, r, p) for i in range(r, x+1)])


def InvNegativeBinomialCD(areaInput: float, rInput: int, pInput: float) -> int:
	InvNegativeBinomialCD_validate(areaInput, rInput, pInput)
	return InvNegativeBinomialCD_calculate(areaInput, rInput, pInput)

def InvNegativeBinomialCD_validate(area: object, r: object, p: object) -> None:
	if not isinstance(area, float) or area < 0 or area > 1:
		raise TypeError("Input value area must be a positive decimal precentage")
	if not isinstance(r, int) or r < 0:
		raise TypeError("Input value r must be positive integer")
	if not isinstance(p, float) or not 0 <= p <= 1:
		raise TypeError("Input value p must be a positive decimal precentage")

def InvNegativeBinomialCD_calculate(area: float, r: int, p: float) -> int:
	cumulative = 0
	i = r
	while cumulative <= area:
		cumulative += NegativeBinomialPD(i, r, p)
		i += 1

	return i - 1