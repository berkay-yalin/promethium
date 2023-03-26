from typing import Union, Any
from math import erf, exp, sqrt, tau
from statistics import _normal_dist_inv_cdf #type:ignore

def NormalPD_validate(x: Any, mu: Any, sigma: Any) -> None:
	if not isinstance(x, (int, float)):
		raise TypeError("Input x value is invalid")
	if not isinstance(mu, (int, float)):
		raise TypeError("Input µ value is invalid")
	if (not sigma) or not isinstance(sigma, (int, float)):
		raise TypeError("Input σ value is invalid")

def NormalPD_calculate(x: float, mu: float, sigma: float) -> float:
	variance = sigma * sigma
	return exp((x - mu) ** 2 / (-2.0 * variance)) / sqrt(tau * variance)

def NormalPD(x: Union[int, float], mu: Union[int, float], sigma: Union[int, float]) -> float:
	NormalPD_validate(x, mu, sigma)
	return NormalPD_calculate(float(x), float(mu), float(sigma))


def NormalCD_calculate(x: float, mu: float, sigma: float) -> float:
	return 0.5 * (1.0 + erf((x - mu) / (sigma * sqrt(2.0))))

def NormalCD(x: Union[int, float], mu: Union[int, float], sigma: Union[int, float]) -> float:
	NormalPD_validate(x, sigma, mu)
	return NormalCD_calculate(float(x), float(mu), float(sigma))


def InvNormalCD_validate(p: Any, mu: Any, sigma: Any) -> None:
	if not isinstance(p, float) or not 0 <= p <= 1:
		raise TypeError("Input p value must be a positive decimal precentage")
	if not isinstance(mu, (int, float)):
		raise TypeError("Input µ value is invalid")
	if not sigma or not isinstance(sigma, (int, float)):
		raise TypeError("Input σ value is invalid")

def InvNormalCD(p: Union[int, float], mu: Union[int, float], sigma: Union[int, float]) -> float:
	InvNormalCD_validate(p, mu, sigma)
	return _normal_dist_inv_cdf(
		float(p),
		float(mu),
		float(sigma)
	) #type:ignore
