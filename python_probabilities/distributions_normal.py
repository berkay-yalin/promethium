from decimal import Decimal
from typing import Union, Any
import math

PI = Decimal(str(math.pi))
EULER = Decimal(str(math.e))

def NormalPD_validate(x: Any, mu: Any, sigma: Any) -> None:
	if not isinstance(x, (int, float)):
		raise TypeError("Input x value is invalid")
	if not isinstance(mu, (int, float)):
		raise TypeError("Input µ value is invalid")
	if not isinstance(sigma, (int, float)):
		raise TypeError("Input σ value is invalid")

def NormalPD_calculate(x: Decimal, mu: Decimal, sigma: Decimal) -> Decimal:
	lhs = (1/(sigma*((PI*2)**(Decimal('0.5')))))
	rhs = (1/(EULER)**(((x-mu)**2)/(2*sigma**2)))
	return(lhs*rhs)

def NormalPD(x: Union[int, float], mu: Union[int, float], sigma: Union[int, float]) -> float:
	NormalPD_validate(x, mu, sigma)
	return float(NormalPD_calculate(
		Decimal(str(x)),
		Decimal(str(mu)),
		Decimal(str(sigma))
	))


def NormalCD_calculate(x: Decimal, mu: Decimal, sigma: Decimal) -> Decimal:
	return Decimal('0.5')*(1+Decimal(str(math.erf((x-mu)/(sigma*(Decimal('2')**Decimal('0.5')))))))

def NormalCD(x: Union[int, float], mu: Union[int, float], sigma: Union[int, float]) -> float:
	NormalPD_validate(x, sigma, mu)
	return float(NormalCD_calculate(
		Decimal(str(x)),
		Decimal(str(mu)),
		Decimal(str(sigma))
	))


def InvNormalCD_validate(p: Any, mu: Any, sigma: Any) -> None:
	if not isinstance(p, float) or not 0 <= p <= 1:
		raise TypeError("Input p value must be a positive decimal precentage")
	if not isinstance(mu, (int, float)):
		raise TypeError("Input µ value is invalid")
	if not isinstance(sigma, (int, float)):
		raise TypeError("Input σ value is invalid")

from statistics import _normal_dist_inv_cdf # type:ignore
def InvNormalCD(p: Union[int, float], mu: Union[int, float], sigma: Union[int, float]) -> float:
	InvNormalCD_validate(p, mu, sigma)
	return _normal_dist_inv_cdf(
		float(p),
		float(mu),
		float(sigma)
	) #type:ignore
