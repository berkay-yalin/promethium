# Promethium 🐍
[![PyPI - Version](https://img.shields.io/pypi/v/promethium.svg)](https://pypi.org/project/promethium)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/promethium.svg)](https://pypi.org/project/promethium)

*Library for calculating statistical distributions, written in pure Python with zero dependencies.*

**Contribution**: [CONTRIBUTING.md](https://github.com/berkay-yalin/promethium/blob/main/CONTRIBUTING.md)

**Documentation**: [README.md](#documentation)

---

## Documentation

- [Binomial Distribution](#binomial-distribution)
  * [Probability mass function](#probability-mass-function)
  * [Cumulative distribution function](#cumulative-distribution-function)
  * [Inverse cumulative distribution function](#inverse-cumulative-distribution-function)
- [Chi-Squared Distribution](#chi-squared-distribution)
  * [Probability density function](#probability-density-function)
  * [Cumulative distribution function](#cumulative-distribution-function-1)
- [Normal Distribution](#normal-distribution)
  * [Probability density function](#probability-density-function-1)
  * [Cumulative distribution function](#cumulative-distribution-function-2)
  * [Inverse cumulative distribution function](#inverse-cumulative-distribution-function-1)
- [Poisson Distribution](#poisson-distribution)
  * [Probability mass function](#probability-mass-function-1)
  * [Cumulative distribution function](#cumulative-distribution-function-3)
  * [Inverse cumulative distribution](#inverse-cumulative-distribution)
- [Geometric Distribution](#geometric-distribution)
  * [Probability mass function](#probability-mass-function-2)
  * [Cumulative distribution function](#cumulative-distribution-function-4)
  * [Inverse cumulative distribution function](#inverse-cumulative-distribution-function-2)

---

## Binomial Distribution
### Probability mass function
```python
binomial.pmf(r, n, p)
```
For the random variable `X` with the binomial distribution `B(n, p)`, calculate the **probability mass function**.\
Where `r` is the number of successes, `n` is the number of trials, and `p` is the probability of success.

**Example**\
To calculate `P(X=7)` for the binomial distribution `X~B(11, 0.33)`:
```python
>>> from promethium import binomial
>>> binomial.pmf(7, 11, 0.33)
0.029656979029412885
```

### Cumulative distribution function
```python
binomial.cdf(r, n, p)
```
For the random variable `X` with the binomial distribution `B(n, p)`, calculate the **cumulative distribution function**.\
Where `r` is the number of successes, `n` is the number of trials, and `p` is the probability of success.

**Example**\
To calculate `P(X≤7)` for the binomial distribution `X~B(11, 0.33)`:
```python
>>> from promethium import binomial.cdf
>>> binomial.cdf(7, 11, 0.33)
0.9912362670526581
```

### Inverse cumulative distribution function
```python
binomial.ppf(q, n, p)
```
For the random variable `X` with the binomial distribution `B(n, p)`, calculate the **inverse** for the **cumulative distribution function**.\
Where `q` is the cumulative probability, `n` is the number of trials, and `p` is the probability of success.

`binomial.ppf(q, n, p)` returns the smallest integer `x` such that `binomial.cdf(x, n, p)` is greater than or equal to `q`.

**Example**\
To calculate the corresponding value for `r` (the number of successes) given the value for `q` (the cumulative probability):
```python
>>> from promethium import binomial
>>> binomial.ppf(0.9912362670526581, 11, 0.333)
7
>>> binomial.cdf(7, 11, 0.333)
0.9912362670526581
```

---

## Chi-Squared Distribution
### Probability density function
```python
chi2.pdf(x, df)
```
Probability density function for the chi-squared distribution `X~X²(df)`,
where `df` is the degrees of the freedom.

### Cumulative distribution function
```python
chi2.cdf(x, df)
```
Cumulative distribution function for the chi-squared distribution `X~X²(df)`,
where `df` is the degrees of the freedom.

**Example**\
To calculate `P(0≤X≤0.556)` for the chi-squared distribution `X~X²(3)`:
```python
>>> from promethium import chi2
>>> chi2.cdf(0.556, 3)
0.09357297231516998
```

---

## Normal Distribution
### Probability density function
```python
normal.pdf(x, µ, σ)
```
Probability density function for the normal distribution `X~N(µ, σ)`.\
Where `µ` is the mean, and `σ` is the standard deviation.

### Cumulative distribution function
```python
normal.cdf(x, µ, σ)
```
Cumulative distribution function for the normal distribution `X~N(µ, σ)`.\
Where `µ` is the mean, and `σ` is the standard deviation.

**Example**\
To calculate `P(X≤0.891)` for the normal distribution `X~N(0.734, 0.114)`:
```python
>>> from promethium import normal
>>> normal.cdf(0.891, 0.734, 0.114)
0.9157737045522477
```

### Inverse cumulative distribution function
```python
normal.ppf(y, µ, σ)
```
Inverse cumulative distribution function for the normal distribution `X~N(µ, σ)`.\
Where `µ` is the mean, and `σ` is the standard deviation.

`normal.ppf(y, µ, σ)` returns the smallest integer `x` such that `normal.cdf(x, µ, σ)` is greater than or equal to `y`.

**Example**\
To calculate the corresponding value for `x` given the value for `y`:
```python
>>> from promethium import normal
>>> normal.ppf(0.9157737045522477, 0.734, 0.114)
0.891
>>> normal.cdf(0.891, 0.734, 0.114)
0.9157737045522477
```

---

## Poisson Distribution
### Probability mass function
```python
poisson.pmf(r, m)
```
For the random variable `X` with the poisson distribution `Po(m)`, calculate the **probability mass function**.\
Where `r` is the number of occurrences, and `m` is the mean rate of occurrence.

**Example**\
To calculate `P(X=7)` for the poisson distribution `X~Po(11.556)`:
```python
>>> from promethium import poisson
>>> poisson(11, 23.445)
0.0019380401123575617
```

### Cumulative distribution function
```python
poisson.cdf(r, m)
```
For the random variable `X` with the poisson distribution `Po(m)`, calculate the **cumulative distribution function**.\
Where `r` is the number of occurrences, and `m` is the mean rate of occurrence.

**Example**\
To calculate `P(X≤7)` for the poisson distribution `X~Po(11.556)`:
```python
>>> from promethium import poisson
>>> poisson.cdf(11, 23.445)
0.0034549033698374467
```

### Inverse cumulative distribution
```python
poisson.ppf(q, m)
```
For the random variable `X` with the poisson distribution `Po(m)`, calculate the **inverse** for the **cumulative distribution function**.\
Where `q` is the cumulative probability, and `m` is the mean rate of occurrence.

`poisson.ppf(q, m)` returns the smallest integer `x` such that `poisson.cdf(x, m)` is greater than or equal to `q`.

**Example**\
To calculate the corresponding value for `r` (number of occurrences) given the values for `q` (cumulative probability):
```python
>>> from promethium import poisson
>>> poisson.ppf(0.0034549033698374467, 23.445)
11
>>> poisson.cdf(11, 23.445)
0.0034549033698374467
```

---

## Geometric Distribution
### Probability mass function
```python
geometric.pmf(x, p)
```
Probability mass function for the geometric distribution `X~G(p)`.\
Where `x` is the number of trials before the first success, and `p` is the probability of success.

**Example**\
To calculate `P(X=3)` for the geometric distribution `X~G(0.491)`:
```python
>>> from promethium import geometric
>>> geometric.pmf(3, 0.491)
0.127208771
```

### Cumulative distribution function
```python
geometric.cdf(x, p)
```
Cumulative distribution function for the geometric distribution `X~G(p)`.\
Where `x` is the number of trials before the first success, and `p` is the probability of success.

**Example**\
To calculate `P(X≤3)` for the geometric distribution `X~G(0.491)`:
```python
>>> from promethium import geometric
>>> geometric.cdf(3, 0.491)
0.868127771
```

### Inverse cumulative distribution function
```python
geometric.ppf(area, p)
```
Inverse cumulative distribution function for the geometric distribution `X~G(p)`.\
Where `x` is the number of trials before the first success, and `p` is the probability of success.

`geometric.ppf(area, p)` returns the smallest integer `x` such that `geometric.cdf(x, p)` is greater than or equal to `area`.

**Example**\
To calculate the corresponding value for `x` given the value for `area`:
```python
>>> from promethium import geometric
>>> geometric.ppf(0.868, 0.491)
3
>> geometric.cdf(3, 0.491)
0.868127771
```

