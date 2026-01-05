### Surprise Relation to Code Length

Surprise is the removal of uncertainty based on observing some event X.
Code length similarly measures the removal of uncertainty after observing a sequence of multiple events.

If I observe event X then Y then Z, by what factor did it collapse my initial probability before observing those events?
It can be derived as the sum of surprise of those events via a small proof below:

$$
P(x_1, x_2, \dots, x_n) = \prod_{i=1}^n P(x_i)
$$

Factor P is reduced by:

$$
\frac{1}{\prod_{i=1}^n P(x_i)}
$$

Code length:

$$
\text{Code Length}
= \log_2 \frac{1}{\prod_{i=1}^n P(x_i)}
= \sum_{i=1}^n \log_2 \frac{1}{p(x_i)}
$$

Code length and surprise are mathematically illuminating the idea of longer binary sequences for less frequent outcomes and shorter binary sequences for frequent outcomes.
This is fundamentally the problem of compression.

The only reason we can compress at all is because different events appear at different frequencies across some distribution P.
Exploiting the varying frequencies of individual events we can group them into sequences that are more probable than others and give them shorter code lengths.

Surprise measures uncertainty of a single event; code length measures uncertainty of a sequence of events.

Entropy therefore is just the expectation of surprise across an entire distribution.

$$
H(X)
= \mathbb{E}[\text{Surprise}(X)]
= \sum_{x \in \mathcal{X}} p(x)\,\text{Surprise}(x)
$$

Substituting the definition of surprise,

$$
\text{Surprise}(x) = \log_2 \frac{1}{p(x)},
$$

we obtain

$$
H(X)
= \sum_{x \in \mathcal{X}} p(x)\,\log_2 \frac{1}{p(x)}
= - \sum_{x \in \mathcal{X}} p(x)\,\log_2 p(x).
$$



It is a code length because it is an expectation: the probability of each event multiplied by the surprise of that event.
It is an expectation of surprise across all events P, i.e. the average code length.


