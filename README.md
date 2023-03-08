# Python Probabilities 🐍
*Library for accurate statistical calculations using Python.*

- [Binomial Distributions](#binomial-distributions)
  - [Binomial Probability Distribution](#binomial-probability-distribution)
  - [Binomial Cumulative Distribution](#binomial-cumulative-distribution)
  - [Inverse Binomial Cumulative Distribution](#inverse-binomial-cumulative-distribution)

## Binomial Distributions
### Binomial Probability Distribution
If a random variable `X` has the binomial distribution `B(n, p)`, then its **probability mass function** can be calculated via `Bpd(r, n, p)`.\
*(where `r` is the number of successes, `n` is the number of trials, and `p` is the probability of success)*

The code below would be to calculate `P(X=7)` for the binomial distribution `X~B(11, 0.33)`.

```python
>>> from python_probabilities import Bpd
>>> Bpd(7, 11, 0.33)
0.0283407102416171981610
```

### Binomial Cumulative Distribution
For the binomial distribution `X~B(n, p)`, the **cumulative probability function** can be calculated via `Bcd(r, n, p)`.\
*(where `r` is the number of successes, `n` is the number of trials, and `p` is the probability of success)*

The code below would be to calculate `P(X≤7)` for the binomial distribution `X~B(11, 0.33)`.

```python
>>> from python_probabilities import Bcd
>>> Bcd(7, 11, 0.33)
0.9917567634324003237640
```

*"A cumulative probability function for a random variable X tells you the sum of all the individual
probabilities up to and including the given value of x in the calculation for P(X < x)".*

### Inverse Binomial Cumulative Distribution
Given the probability for a cumulative probability function, the value for `r` (number of successes) can be calculated via `InvB(x, n, p)`.\
*(where `x` is the probability, `n` is the number of trials, and `p` is the probability of success)*

```python
>>> from python_probabilities import *
>>> InvB(0.9917567634, 11, 0.33)
7
>>> Bcd(7, 11, 0.33)
0.9917567634324003237640
```
