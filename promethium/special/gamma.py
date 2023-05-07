"""
Reimplementation of the stdlib gammainc function in Python.

JavaScript implementation from the stdlib library:
    https://github.com/stdlib-js/math-base-special-gammainc/blob/dfe83f6926e872018d5276f0b801b15fc24614a6/lib/main.js

Original C++ code from Boost library:
    https://www.boost.org/doc/libs/1_62_0/boost/math/special_functions/gamma.hpp


* @license Apache-2.0
*
* Copyright (c) 2018 The Stdlib Authors.
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*    http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.


//  Copyright John Maddock 2006-7, 2013-14.
//  Copyright Paul A. Bristow 2007, 2013-14.
//  Copyright Nikhar Agrawal 2013-14
//  Copyright Christopher Kormanyos 2013-14

//  Use, modification and distribution are subject to the
//  Boost Software License, Version 1.0. (See accompanying file
//  LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
"""

from typing import List, Union
from math import exp, erfc, gamma, sqrt, log
import math


FLOAT32_SMALLEST_NORMAL = 1.1754943508222875e-38
FLOAT64_EPSILON = 2.2204460492503130808472633361816E-16
MAX_ITER = 1_000_000


def finiteGammaQ(a: int, x: float) -> float:
    term: float = 0.0
    _sum: float = 0.0

    e = exp(-x)
    _sum = e

    if _sum != 0.0:
        term = _sum
        for i in range(1, a):
            term /= i
            term *= x
            _sum += term
    return _sum



def finiteHalfGammaQ(a: float, x: float) -> float:
    ''' Calculates normalized Q when a is a half-integer. '''
    half = 0.0
    term = 0.0
    _sum = 0.0

    e = erfc(sqrt(x))

    if e != 0.0 and a > 1.0:
        term = exp(-x) / sqrt(math.pi * x)
        term *= x
        half = 0.5
        term /= half
        _sum = term

        # shouldn't really be int(a) but works for now
        for i in range(2, int(a)):
            term /= i - half
            term *= x
            _sum += term
        e += _sum        
    return e



def fullIGammaPrefix(a: float, z: float) -> float:
    ''' Calculates the power term prefix `(z^a)(e^-z)` used in the non-normalized incomplete gammas. '''
    return pow(z, a) * math.exp(-z)



def polyvalC0( x ):
    if ( x == 0.0 ):
        return -0.3333333333333333
    return -0.3333333333333333 + (x * (0.08333333333333333 + (x * (-0.014814814814814815 + (x * (0.0011574074074074073 + (x * (0.0003527336860670194 + (x * (-0.0001787551440329218 + (x * (0.00003919263178522438 + (x * (-0.0000021854485106799924 + (x * (-0.00000185406221071516 + (x * (8.296711340953087e-7 + (x * (-1.7665952736826078e-7 + (x * (6.707853543401498e-9 + (x * (1.0261809784240309e-8 + (x * (-4.382036018453353e-9 + (x * 9.14769958223679e-10)))))))))))))))))))))))))))

def polyvalC1( x ):
    if ( x == 0.0 ):
        return -0.001851851851851852    
    return -0.001851851851851852 + (x * (-0.003472222222222222 + (x * (0.0026455026455026454 + (x * (-0.0009902263374485596 + (x * (0.00020576131687242798 + (x * (-4.018775720164609e-7 + (x * (-0.000018098550334489977 + (x * (0.00000764916091608111 + (x * (-0.0000016120900894563446 + (x * (4.647127802807434e-9 + (x * (1.378633446915721e-7 + (x * (-5.752545603517705e-8 + (x * 1.1951628599778148e-8)))))))))))))))))))))))

def polyvalC2( x ):
    if ( x == 0.0 ):
        return 0.004133597883597883    
    return 0.004133597883597883 + (x * (-0.0026813271604938273 + (x * (0.0007716049382716049 + (x * (0.0000020093878600823047 + (x * (-0.00010736653226365161 + (x * (0.000052923448829120125 + (x * (-0.000012760635188618728 + (x * (3.423578734096138e-8 + (x * (0.0000013721957309062932 + (x * (-6.298992138380055e-7 + (x * 1.4280614206064242e-7)))))))))))))))))))

def polyvalC3( x ):
    if ( x == 0.0 ):
        return 0.0006494341563786008
    return 0.0006494341563786008 + (x * (0.00022947209362139917 + (x * (-0.0004691894943952557 + (x * (0.00026772063206283885 + (x * (-0.00007561801671883977 + (x * (-2.396505113867297e-7 + (x * (0.000011082654115347302 + (x * (-0.0000056749528269915965 + (x * 0.0000014230900732435883)))))))))))))))

def polyvalC4( x ):
    if ( x == 0.0 ):
        return -0.0008618882909167117    
    return -0.0008618882909167117 + (x * (0.0007840392217200666 + (x * (-0.0002990724803031902 + (x * (-0.0000014638452578843418 + (x * (0.00006641498215465122 + (x * (-0.00003968365047179435 + (x * 0.000011375726970678419)))))))))))

def polyvalC5( x ):
    if ( x == 0.0 ):
        return -0.00033679855336635813    
    return -0.00033679855336635813 + (x * (-0.00006972813758365858 + (x * (0.0002772753244959392 + (x * (-0.00019932570516188847 + (x * (0.00006797780477937208 + (x * (1.419062920643967e-7 + (x * (-0.000013594048189768693 + (x * (0.000008018470256334202 + (x * -0.000002291481176508095)))))))))))))))

def polyvalC6( x ):
    if ( x == 0.0 ):
        return 0.0005313079364639922    
    return 0.0005313079364639922 + (x * (-0.0005921664373536939 + (x * (0.0002708782096718045 + (x * (7.902353232660328e-7 + (x * (-0.00008153969367561969 + (x * (0.0000561168275310625 + (x * -0.000018329116582843375)))))))))))

def polyvalC7( x ):
    if ( x == 0.0 ):
        return 0.00034436760689237765    
    return 0.00034436760689237765 + (x * (0.00005171790908260592 + (x * (-0.00033493161081142234 + (x * (0.0002812695154763237 + (x * -0.00010976582244684731)))))))

def polyvalC8( x ):
    if ( x == 0.0 ):
        return -0.0006526239185953094    
    return -0.0006526239185953094 + (x * (0.0008394987206720873 + (x * -0.000438297098541721)))

def evalpoly(c: List[float], x: float) -> float:
    """
    Evaluates a polynomial
    e.g. var v = evalpoly( [3.0,2.0,1.0], 10.0 ); // 3*10^0 + 2*10^1 + 1*10^2
    """

    i = len(c)

    if i < 2 or x == 0.0:
        if i == 0.0:
            return 0.0
        return c[0]
    
    i -= 1
    p = ( c[ i ] * x ) + c[ i - 1 ]
    i -= 2;
    while ( i >= 0 ):
        p = ( p * x ) + c[ i ]
        i -= 1
    return p;

def igammaTemmeLarge(a: float, x: float) -> float:
    """Asymptotic expansions of the incomplete gamma functions when `a` is large and `x ~ a` (IEEE double precision or 10^-17)"""
    workspace = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]

    sigma = (x - a) / a
    phi = -log(1.0 + sigma) + sigma
    y = a * phi
    z = sqrt( 2.0 * phi)

    if x < a:
        z = -z

    workspace[ 0 ] = polyvalC0( z )
    workspace[ 1 ] = polyvalC1( z )
    workspace[ 2 ] = polyvalC2( z )
    workspace[ 3 ] = polyvalC3( z )
    workspace[ 4 ] = polyvalC4( z )
    workspace[ 5 ] = polyvalC5( z )
    workspace[ 6 ] = polyvalC6( z )
    workspace[ 7 ] = polyvalC7( z )
    workspace[ 8 ] = polyvalC8( z )
    workspace[ 9 ] = -0.00059676129019274625

    result = evalpoly(workspace, 1.0 / a)
    result *= exp(-y) / sqrt( 2 * math.pi * a)
    
    if x < a:
        result = -result
    result += erfc(sqrt(y)) / 2.0
    return result



def sumSeries(generator, initialValue: float = 0.0):
    FLOAT64_EPSILON = 2.2204460492503130808472633361816E-16
    MAX_TERMS = 1_000_000

    tolerance = FLOAT64_EPSILON
    counter = MAX_TERMS

    nextTerm = generator.next()
    result = initialValue + nextTerm

    while abs(tolerance * result) < abs(nextTerm) and counter != 0:
        nextTerm = generator.next()
        result += nextTerm
        counter -= 1
    return result



class _lowerIncompleteGammaSeries(object):
    a: float
    z: float
    result: float

    def __init__(self, a1: float, z1: float) -> None:
        self.a = a1
        self.z = z1
        self.result = 1.0
    
    def next(self) -> float:
        r = self.result
        self.a += 1.0
        self.result *= self.z / self.a
        return r

def lowerGammaSeries(a: float, z: float, initialValue: float = 0.0) -> float:
    """
    Sums elements of the series expansion of the lower incomplete gamma function.
    Multiply result by `((z^a) * (e^-z) / a)` to get the full lower incomplete integral.
    Divide by `tgamma(a)` to get the normalized value.
    """

    result = 0.0

    s = _lowerIncompleteGammaSeries(a, z)
    result = sumSeries(s, initialValue)
    return result



def regularisedGammaPrefix(a: float, z: float) -> float:
    ''' Computes (z^a)*(e^-z) / gamma(a) '''
    return ( pow(z, a) * math.exp(-z) ) / math.gamma(a)



def gamma1pm1(x: Union[int, float]) -> float:
    """calculate gamma(x + 1) - 1"""
    return gamma(x + 1) - 1

class _smallGamma2Series(object):
    a: float
    x: float

    result: float
    apn: float
    n: float
    r: float

    def __init__(self, _a: float, _x: float) -> None:
        self.a = _a
        self.x = _x

        self.result = -self.x
        self.x = -self.x
        self.apn = self.a + 1.0
        self.n = 1

    def next(self) -> float:
        r = self.result / self.apn
        self.result *= self.x
        self.n += 1
        self.result /= self.n
        self.apn += 1.0
        return r

def tgammaSmallUpperPart(a, x, invert = False):
    result = gamma1pm1(a)
    pgam = (result + 1.0) / a
    p = (x ** a) - 1
    result -= p
    result /= a
    s = _smallGamma2Series(a, x)
    p += 1.0

    if invert:
        initialValue = pgam
    else:
        initialValue = 0.0

    result = (-p) * sumSeries(s, (initialValue - result) / p)

    if invert:
        result = -result
    return [result, pgam]



def continuedFractionA(gen, factor, maxIter):
    delta = 0.0
    v = gen.next()
    f = v[1]
    a0 = v[0]
    if f == 0.0:
        f = FLOAT32_SMALLEST_NORMAL
    C = f
    D = 0.0

    while maxIter > 0:
        v = gen.next()
        if v:
            D = v[1] + (v[0] * D)
            if D == 0.0:
                D = FLOAT32_SMALLEST_NORMAL

            C = v[1] + (v[0] / C)
            if C == 0.0:
                C = FLOAT32_SMALLEST_NORMAL

            D = 1.0 / D
            delta = C * D
            f *= delta

            if abs(delta - 1.0) <= factor:
                break
        else:
            break
        maxIter -= 1

    return a0 / f

# def continuedFractionB(gen, factor, maxIter):
#     v = gen.next()
#     f = v[1]
#
#     if f == 0.0:
#         f = FLOAT32_SMALLEST_NORMAL
#
#     C = f
#     D = 0.0
#
#     v = gen.next()
#     if v:
#         D = v[1] + (v[0] * D)
#         if D == 0.0:
#             D = FLOAT32_SMALLEST_NORMAL
#         C = v[1] + (v[0] / C)
#         if C == 0.0:
#             C = FLOAT32_SMALLEST_NORMAL
#         D = 1.0 / D
#         delta = C * D
#         f *= delta
#
#     while v and abs(delta - 1.0) > factor and maxIter > 0:
#         v = gen.next()
#         if v:
#             D = v[1] + (v[0] * D)
#             if D == 0.0:
#                 D = FLOAT32_SMALLEST_NORMAL
#             C = v[1] + (v[0] / C)
#             if C == 0.0:
#                 C = FLOAT32_SMALLEST_NORMAL
#             D = 1.0 / D
#             delta = C * D
#             f *= delta
#         maxIter -= 1
#     return f

def continuedFraction(_generator, _opts = {}) -> float:
    """ Evaluates the continued fraction approximation for the supplied
    series generator using the modified Lentz algorithm. """

    # if _opts == {}:
    #     opts = { 'tolerance': FLOAT64_EPSILON, 'maxIter': MAX_ITER }
    # else:
    #     opts = _opts

    opts = { 'tolerance': FLOAT64_EPSILON, 'maxIter': MAX_ITER }

    # if 'keep' in opts:
    #     return continuedFractionA(_generator, opts['tolerance'], opts['maxIter'])
    return continuedFractionA(_generator, opts['tolerance'], opts['maxIter'])

class _upperIncompleteGammaFrac:
    a: float
    z: float
    k: float

    def __init__(self, _a: float, _z: float) -> None:
        self.z = _z - _a + 1.0
        self.a = _a
        self.k = 0.0

    def next(self) -> List[float]:
        self.k += 1.0
        self.z += 2.0
        return [self.k * (self.a - self.k), self.z]

def upperGammaFraction(a: float, z: float) -> float:
    f = _upperIncompleteGammaFrac(a, z)
    return 1.0 / (z - a + 1.0 + continuedFraction(f))



def gammainc(x: float, a: float, regularized: bool = True, upper: bool = False) -> float:
    NaN = float('NaN')
    SQRT_EPSILON = 0.1490116119384765625e-7
    FLOAT64_MAX = 1.7976931348623157e+308
    # SQRT_TWO_PI = 2.506628274631000502415765284811045253e+00
    MAX_LN = 709.782712893384
    # PINF = float('inf')
    # MAX_FACTORIAL = 170

    # x: non-negative number
    # a: positive number
    if x < 0.0 or a <= 0.0:
        return NaN

    normalized: bool = regularized
    invert: bool = upper
    result: float = 0.0

    # if (a >= MAX_FACTORIAL) and (not normalized):
    #     if (invert) and (a * 4.0 < x):
    #         result = (a * math.log(x)) - x
    #         result += math.log( upperGammaFraction(a, x) )
    #     elif (not invert) and (a > 4.0 * x):
    #         result = ( a * math.log(x) ) - x
    #         initValue = 0.0
    #         result += math.log( lowerGammaSeries(a, x, initValue) / a )
    #     else:
    #         result = gammainc(a, x, True, invert)
    #         if result == 0.0:
    #             if invert:
    #                 result = 1.0 + (1.0 / (12.0 * a)) + (1.0 / (288.0 * a * a))
    #                 result = math.log(result) - a + ((a - 0.5) * math.log(a))
    #                 result += math.log(SQRT_TWO_PI)
    #             else:
    #                 result = (a * math.log(x)) - x
    #                 initValue = 0.0
    #                 result += math.log( lowerGammaSeries(a, x, initValue) / a)
    #         else:
    #             result = math.log(result) + math.lgamma(a)
    #     if result > MAX_LN:
    #         return PINF
    #     return math.exp(result)

    isSmallA = a < 30 and a <= x + 1.0 and x < MAX_LN
    if isSmallA:
        fa = math.floor(a)
        isInt = fa == a #int being compared to float
        isHalfInt = False if isInt else math.fabs(fa - a) == 0.5
    else:
        # isInt = isHalfInt = False
        isInt = False
        isHalfInt = False

    if isInt and x > 0.6:
        invert = not invert
        evalMethod = 0
    elif isHalfInt and x > 0.2:
        invert = not invert
        evalMethod = 1
    elif x < SQRT_EPSILON and a > 1.0:
        evalMethod = 6
    elif x < 5.0:
        if -0.4 / math.log(x) < a:
            evalMethod = 2
        else:
            evalMethod = 3
    elif x < 1.1:
        if (x * 0.75) < a:
            evalMethod = 2
        else:
            evalMethod = 3
    else:
        # Begin by testing whether we're in the "bad" zone where the result will be near 0.5 and the usual series and continued fractions are slow to converge:
        useTemme = False
        if normalized and a > 20:
            sigma = abs( (x - a) / a )
            if a > 200:
                if 20 / a > sigma * sigma:
                    useTemme = True
            elif sigma < 0.4:
                useTemme = True        
        if useTemme:
            evalMethod = 5
        elif  x - (1.0 / (3.0 * x)) < a:
            evalMethod = 2
        else:
            evalMethod = 4
            invert = not invert

    if evalMethod == 0:
        result = finiteGammaQ(a, x)
        if normalized == False:
            result *= math.gamma(a)
 
    elif evalMethod == 1:
        result = finiteHalfGammaQ(a, x)
        if normalized == False:
            result *= math.gamma(a)
    
    elif evalMethod == 2:
        result = regularisedGammaPrefix(a, x) if normalized else fullIGammaPrefix(a, x)

        if result != 0.0:
            initValue = 0.0
            optimisedInvert = False

            if invert:
                initValue = 1.0 if normalized else math.gamma(a)

                if normalized or result >= 1.0 or FLOAT64_MAX * result > initValue:
                    initValue /= result

                    if normalized or a < 1.0 or FLOAT64_MAX / a > initValue:
                        initValue *= -a
                        optimisedInvert = True
                    else:
                        initValue = 0.0
                else:
                    initValue = 0.0
        
        result *= lowerGammaSeries(a, x, initValue) / a

        if optimisedInvert:
            invert = False
            result = -result

    elif evalMethod == 3:
        invert = not invert
        res = tgammaSmallUpperPart(a, x, invert)
        result = res[0]
        g = rest[1]
        invert = False
        if normalized:
            result /= g

    elif evalMethod == 4:
        result = regularisedGammaPrefix(a, x) if normalized else fullIGammaPrefix(a, x)
        if result != 0.0:
            result *= upperGammaFraction(a, x)

    elif evalMethod == 5:
        result = igammaTemmeLarge(a, x)
        if x >= a:
            invert = not invert

    elif evalMethod == 6:
        if normalized:
            result = (x ** a) / math.gamma(a + 1.0)
        else:
            result = (x ** a) / a
        result *= 1.0 - (a * x / (a + 1.0))
    
    if normalized and result > 1.0:
        result = 1.0

    if invert:
        gam = 1.0 if normalized else math.gamma(a)
        result = gam - result
    
    return result

