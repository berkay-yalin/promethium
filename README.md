# Python Probabilities 🐍
*Library for accurate statistical calculations using Python.*

- [Binomial Distributions](#binomial-distributions)
  - [Probability mass function](#probability-mass-function)
  - [Cumulative distribution function](#cumulative-distribution-function)
  - [Inverse cumulative distribution function](#inverse-cumulative-distribution-function)
- [Poisson Distributions](#poisson-distributions)
  - [Poisson Probability Distribution](#poisson-probability-distribution)
  - [Poisson Cumulative Distribution](#poisson-cumulative-distribution)
  - [Inverse Poisson Cumulative Distribution](#inverse-poisson-cumulative-distribution)

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
InvBinomial(q, n, p)
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
### Poisson Probability Distribution
If a random variable `X` has the poisson distribution `Po(λ)`, then its **probability mass function** can be calculated via `Ppd(k, λ)`.\
*(where `k` is the number of occurrences and `λ` is the expected number of occurrences)*

The code below would be to calculate `P(X=3)` for the binomial distribution `X~Po(6)`.

```python
>>> from python_probabilities import Ppd
>>> Ppd(3, 6)
0.08923507835998894
```

### Poisson Cumulative Distribution
For the binomial distribution `X~Po(λ)`, the **cumulative probability function** can be calculated via `Pcd(k, λ)`.\
*(where `k` is the number of occurrences and `λ` is the expected number of occurrences)*

The code below would be to calculate `P(X≤3)` for the binomial distribution `X~Po(6)`.

```python
>>> from python_probabilities import Pcd
>>> Pcd(3, 6)
0.15120388277664792
```

*"A cumulative probability function for a random variable X tells you the sum of all the individual
probabilities up to and including the given value of x in the calculation for P(X < x)".*

### Inverse Poisson Cumulative Distribution
Given the probability for a cumulative probability function, the value for `k` (number of occurrences) can be calculated via `InvP(x, λ)`.\
*(where `x` is the probability and `λ` is the expected number of occurrences)*

```python
>>> from python_probabilities import *
>>> InvP(0.4, 8)
7
>>> Pcd(7, 8)
0.4529608094869947
```
