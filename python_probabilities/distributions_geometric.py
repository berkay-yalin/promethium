from decimal import Decimal

def GeometricPD(x: int, p: float) -> Decimal:
	GeometricPD_validate(x, p)
	return GeometricPD_calculate(x, Decimal(str(p)))

def GeometricPD_validate(x: object, p: object) -> None:
	if not isinstance(x, int) or x < 0:
		raise TypeError("Input value x must be positive integer")
	if not isinstance(p, float) or not 0 <= p <= 1:
		raise TypeError("Input value p must be a float between 0 and 1")

def GeometricPD_calculate(x: int, p: Decimal) -> Decimal:
	return ((1-p) ** (x-1)) * p


def GeometricCD(x: int, p: float) -> Decimal:
	GeometricPD_validate(x, p)
	return GeometricCD_calculate(x, Decimal(str(p)))

def GeometricCD_calculate(x: int, p: Decimal) -> Decimal:
	return 1 - (1 - p) ** x


def InvGeometricCD(area: float, p: float) -> int:
	InvGeometricCD_validate(area, p)
	return InvGeometricCD_calculate(area, p)

def InvGeometricCD_validate(area: object, p: object) -> None:
	if not isinstance(area, float) or area < 0 or area > 1:
		raise TypeError("Input value area must be a positive decimal precentage")
	if not isinstance(p, float) or not 0 <= p <= 1:
		raise TypeError("Input value p must be a float between 0 and 1")

def InvGeometricCD_calculate(area: float, p: float) -> int:
	cumulative = 0
	i = 1
	while cumulative <= area:
		cumulative += GeometricPD(i, p)
		i += 1
	return i - 1
