from python_probabilities import *
from typing import Any

geometricTestData = (
    {
        'values': (6, 0.2435, 0.05),
        'expected': {
                'Gpd': 0.06033143,
                'Gcd': 0.81256374,
                'InvG': 1
        }
    },
    {
        'values': (8, 0.3587, 0.8),
        'expected': {
                'Gpd': 0.01600147,
                'Gcd': 0.97139184,
                'InvG': 4
        }
    }
)

def GeometricTesting(function: str, testdata: Any):
    print(f"### TESTING {function.upper()} DISTRIBUTIONS ###")
    for i in testdata:
        x = i['values'][0]
        p = i['values'][1]
        area = i['values'][2]

        if function == 'Gpd':
                observed = GeometricPD(x, p)
                expected= i['expected']['Gpd']
        elif function == 'Gcd':
                observed = GeometricCD(x, p)
                expected = i['expected']['Gcd']
        elif function == 'InvG':
                observed = InvGeometricCD(area, p)
                expected = i['expected']['InvG']
        else:
                raise SystemExit('what are you doing??')

        precision = len(str(expected))
        if str(observed)[:precision] == str(expected):
            print(f"success!\n  {observed}\n≈ {expected}")
        else:
            print(f"fail! \n   {observed}\n!= {expected}")
        print('### TESTING COMPLETE ###')

GeometricTesting('Gpd', geometricTestData)
GeometricTesting('Gcd', geometricTestData)
GeometricTesting('InvG', geometricTestData)
GeometricTesting('Drake', geometricTestData)

