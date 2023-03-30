# Python Probabilities 🐍
*Library for accurate statistical calculations using Python.*

- [Binomial Distributions](#binomial-distributions)
  - [Probability mass function](#probability-mass-function)
  - [Cumulative distribution function](#cumulative-distribution-function)
  - [Inverse cumulative distribution function](#inverse-cumulative-distribution-function)
- [Poisson Distributions](#poisson-distributions)
  - [Probability mass function](#probability-mass-function-1)
  - [Cumulative distribution function](#cumulative-distribution-function-1)
  - [Inverse cumulative distribution](#inverse-cumulative-distribution)

## Binomial Distributions
### Probability mass function
```python
BinomialPD(r, n, p)
```
For the random variable `X` with the binomial distribution `B(n, p)`, calculate the **probability mass function**.\
Where `r` is the number of successes, `n` is the number of trials, and `p` is the probability of success.

**Example**\
To calculate `P(X=7)` for the binomial distribution `X~B(11, 0.33)`:
```python
>>> from python_probabilities import BinomialPD
>>> BinomialPD(7, 11, 0.33)
0.029656979029412885
```
---
### Cumulative distribution function
```python
BinomialCD(r, n, p)
```
For the random variable `X` with the binomial distribution `B(n, p)`, calculate the **cumulative distribution function**.\
Where `r` is the number of successes, `n` is the number of trials, and `p` is the probability of success.

**Example**\
To calculate `P(X≤7)` for the binomial distribution `X~B(11, 0.33)`:
```python
>>> from python_probabilities import BinomialCD
>>> BinomialCD(7, 11, 0.33)
0.9912362670526581
```
---
### Inverse cumulative distribution function
```python
InvBinomialCD(q, n, p)
```
For the random variable `X` with the binomial distribution `B(n, p)`, calculate the **inverse** for the **cumulative distribution function**.\
Where `q` is the cumulative probability, `n` is the number of trials, and `p` is the probability of success.

`InvBinomialCD(q, n, p)` returns the smallest integer `x` such that `BinomialCD(x, n, p)` is greater than or equal to `q`.

**Example**\
To calculate the corresponding value for `r` (the number of successes) given the value for `q` (the cumulative probability):
```python
>>> from python_probabilities import BinomialCD, InvBinomialCD
>>> InvBinomialCD(0.9912362670526581, 11, 0.333)
7
>>> BinomialCD(7, 11, 0.333)
0.9912362670526581
```

## Poisson Distributions
### Probability mass function
```python
PoissonPD(r, m)
```
For the random variable `X` with the poisson distribution `Po(m)`, calculate the **probability mass function**.\
Where `r` is the number of occurrences, and `m` is the mean rate of occurrence.

**Example**\
To calculate `P(X=7)` for the poisson distribution `X~Po(11.556)`:
```python
>>> from python_probabilities import PoissonPD
>>> PoissonPD(11, 23.445)
0.0019380401123575617
```
---
### Cumulative distribution function
```python
PoissonCD(r, m)
```
For the random variable `X` with the poisson distribution `Po(m)`, calculate the **cumulative distribution function**.\
Where `r` is the number of occurrences, and `m` is the mean rate of occurrence.

**Example**\
To calculate `P(X≤7)` for the poisson distribution `X~Po(11.556)`:
```python
>>> from python_probabilities import PoissonCD
>>> PoissonCD(11, 23.445)
0.0034549033698374467
```
---
### Inverse cumulative distribution
```python
InvPoissonCD(q, m)
```
For the random variable `X` with the poisson distribution `Po(m)`, calculate the **inverse** for the **cumulative distribution function**.\
Where `q` is the cumulative probability, and `m` is the mean rate of occurrence.

`InvPoissonCD(q, m)` returns the smallest integer `x` such that `PoissonCD(x, m)` is greater than or equal to `q`.

**Example**\
To calculate the corresponding value for `r` (number of occurrences) given the values for `q` (cumulative probability):
```python
>>> from python_probabilities import PoissonCD, InvPoissonCD
>>> InvPoissonCD(0.0034549033698374467, 23.445)
11
>>> PoissonCD(11, 23.445)
0.0034549033698374467
```
