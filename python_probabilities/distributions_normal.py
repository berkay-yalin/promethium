from decimal import Decimal
from typing import Union, Any
import math

PI = Decimal(str(math.pi))
EULER = Decimal(str(math.e))

def NormalPD_validate(x: Any, sd: Any, mu: Any) -> None:
	if not isinstance(x, (int, float)):
		raise TypeError("Input x value is invalid")
	if not isinstance(mu, (int, float)):
		raise TypeError("Input µ value is invalid")
	if not isinstance(sd, (int, float)):
		raise TypeError("Input σ value is invalid")

def NormalPD_calculate(x: Decimal, sd: Decimal, mu: Decimal) -> Decimal:
	lhs = (1/(sd*((PI*2)**(Decimal('0.5')))))
	rhs = (1/(EULER)**(((x-mu)**2)/(2*sd**2)))
	return(lhs*rhs)

def NormalPD(x: Union[int, float], sd: Union[int, float], mu: Union[int, float]) -> float:
	NormalPD_validate(x, sd, mu)
	return float(NormalPD_calculate(
		Decimal(str(x)),
		Decimal(str(sd)),
		Decimal(str(mu))
	))

def NormalCD_calculate(x: Decimal, mu: Decimal, sd: Decimal) -> Decimal:
	return Decimal('0.5')*(1+Decimal(str(math.erf((x-mu)/(sd*(Decimal('2')**Decimal('0.5')))))))

def NormalCD(x: Union[int, float], sd: Union[int, float], mu: Union[int, float]) -> float:
	NormalPD_validate(x, sd, mu)
	return float(NormalCD_calculate(
		Decimal(str(x)),
		Decimal(str(mu)),
		Decimal(str(sd))
	))


# def InvNormalCD_validate(tail: object, area: object, sd:object, mean:object):
# 	if not isinstance(area, float):
# 		raise TypeError("Input value area must be float")
# 	if area < 0 or area > 1:
# 		raise ValueError("Input value area out of domain")
# 	if not isinstance(tail, str):
# 		raise ValueError("Input value tail must be L, R or C")
# 	if tail not in ['L','R','C','l','r','c']:
# 		raise ValueError("Input value tail must be L, R or C")
# 	if not isinstance(mean, (int,float)):
# 		raise TypeError("Input mean value is invalid")
# 	if not isinstance(sd, (int,float)):
# 		raise TypeError("Input sd value is invalid")

# def InvNormalCD_calculate(tail: object, area: object, sd: object, mean: object):
# 	pass

# def InvNormalCD(tail: object, area: object, sd: object, mean: object):
# 	InvPoissonCD_validate(tail, area, sd, mean)
# 	return InvPoissonCD_calculate(tail, area, sd, mean)
