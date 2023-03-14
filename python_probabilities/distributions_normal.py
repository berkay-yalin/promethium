from fractions import Fraction
import math

def NormalPD_validate(mean: object, sd: object, x: object) -> None:
	if not isinstance(mean, (int,float)):
		raise TypeError("Input mean value is invalid")
	if not isinstance(sd, (int,float)):
		raise TypeError("Input sd value is invalid")
	if not isinstance(x, (int, float)):
		raise TypeError("Input x value is invalid")

def NormalPD_calculate(x: float, mean: float, sd: float) -> float:
	lhs = (1/(sd*((math.pi*2)**(1/2))))
	rhs = (1/(math.e)**(((x-mean)**2)/(2*sd**2)))
	return(lhs*rhs)

def NormalPD(x: float, mean: float, sd: float) -> float:
	NormalPD_validate(x, mean, sd)
	return NormalPD_calculate(x, mean, sd)


def NormalCD_calculate(x: float, mean: float, sd: float) -> float:
	return 0.5*(1+math.erf((x-mean)/(sd*(2**0.5))))

def NormalCD(x: float, mean: float, sd: float) -> float:
	NormalPD_validate(x, mean, sd)
	return NormalCD_calculate(x, mean, sd)


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
