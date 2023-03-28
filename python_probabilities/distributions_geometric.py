from decimal import Decimal
import math

def GeometricPD(xInput: int, pInput: float) -> Decimal:
	GeometricPD_validate(xInput, pInput)
	return GeometricPD_calculate(xInput, Decimal(str(pInput)))

def GeometricPD_validate(x: object, p: object) -> None:
	if not isinstance(x, int) or x < 0:
		raise TypeError("Input value x must be positive integer")
	if not isinstance(p, float) or not 0 <= p <= 1:
		raise TypeError("Input value p must be a non-negative float")

def GeometricPD_calculate(x: int, p: Decimal) -> Decimal:
	return ((1-p)**(x-1))*p


def GeometricCD(xInput: int, pInput: float) -> Decimal:
	GeometricPD_validate(xInput, pInput)
	return GeometricCD_calculate(xInput, pInput)

def GeometricCD_calculate(x: int, p: Decimal) -> Decimal:
	return 1 - (1-p)**x


def InvGeometricCD(areaInput: float, pInput: float) -> int:
	InvGeometricCD_validate(areaInput, pInput)
	return InvGeometricCD_calculate(areaInput, pInput)

def InvGeometricCD_validate(area: object, p: object) -> None:
	if not isinstance(area, float) or area < 0 or area > 1:
		raise TypeError("Input value area must be a positive decimal precentage")
	if not isinstance(p, float) or not 0 <= p <= 1:
		raise TypeError("Input value p must be a positive decimal precentage")

def InvGeometricCD_calculate(area: float, p: float) -> int:
	cumulative = 0
	i = 1
	while cumulative <= area:
		cumulative += GeometricPD(i, p)
		i += 1
	return i - 1
