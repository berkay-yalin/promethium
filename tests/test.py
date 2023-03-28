from python_probabilities import *
GeometricPD

geometricTestData = (
	  {
			'values': (6, 0.2435, 0.05),
			'expected': {
				  'Gpd': 0.06033143,
				  'Gcd': 0.81256374,
				  'InvG': 0.7138929909
			}
	  }

	  {
			'values': (50, 0.0567, 0.08),
			'expected': {
				  'Gpd': 0.06033143,
				  'Gcd': 0.81256374,
				  'InvG': 0.7138929909
			}
	  }
)


def GeometricTesting(function: str, testdata: Any):
	  print(f"### TESTING {function.upper()} DISTRIBUTIONS ###")
	  for i in testdata:
			x = i['values'][0]
			p = i['values'][1]`
			area = i['values'][2]
			if function == 'Gpd':
				  observed: float = GeometricPD(x,p])
				  expected: float = i['expected']['Gpd']
			elif function == 'Gcd':
				  observed: float = GeometricCD(*x,p)
				  expected: float = i['expected']['Ncd']
			elif function == 'InvG':
				  observed: float = InvGeometricCD(area, p)
				  expected: float = i['expected']['InvN']
			else:
				  raise SystemExit('what are you doing??')

			precision = len(str(expected).split('.')[-1])

			if round(observed, precision) == expected:

				  print(f"success!\n  {observed}\n≈ {expected}")

			else:

				  print(f"fail! \n   {observed}\n!= {expected}")

	  print('### TESTING COMPLETE ###')
