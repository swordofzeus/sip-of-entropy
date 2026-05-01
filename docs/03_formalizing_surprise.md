## Formula for Surprise

Surprise links the collapse of the remaining probability mass after seeing a new event X to a unit of information (bits).

Lets say we are rolling a 4 sided die with a 40% chance of 1, 20% chance of 2,3 and 4.
There are 4^n such sequences. Assume we roll the dice 4 times there are:

$$
4^4 = 256
$$

different outcomes.

Example outcomes:
- (1,1,2,4)
- (1,2,2,4)
- (2,1,2,4)

We'll derive the formula for surprise by examining the surprise of rolling a 1 on the first outcome.

Before we roll there are 256 possible outcomes. 40% of probability mass is reserved for outcomes beginning with 1, of which there are:

$$
1 \cdot 4 \cdot 4 \cdot 4 = 64
$$

There are:

$$
3 \cdot 4 \cdot 4 \cdot 4 = 192
$$

outcomes that do not begin with 1.

| Case | Description | Number of Outcomes | Probability Mass |
|----|-------------|-------------------|------------------|
| X = 1 | Outcomes beginning with 1 | 64 | 0.4 |
| X ≠ 1 | Outcomes not beginning with 1 | 192 | 0.6 |

Before any roll: (0, 1.0)

There exist two worlds before our roll: one where event X = 1 occurs and one where X = 1 did not occur.
Notice surprise does not depend on how many other outcomes there are, it depends solely on the probability of the target outcome because conceptually it eliminates the probability mass from observing X, not zooming into the mass of an event not involving X.

If we roll X = 1, it eliminates 60% of the remaining probability mass. So we arrive at the interval:

(0, 0.4)

So the factor by which our probability distribution collapsed was from 1 previously to 0.4. The ratio is:

$$
\frac{1}{0.4} = 2.5
$$

Another way to think about how much probability mass was eliminated is to move from a ratio to bits. Assume for a second we have a much smaller number of possible sequences before our 2nd roll:

- (1,2,1,1)
- (1,4,4,4)
- (1,2,2,2)
- (1,1,1,1)

We roll a 2. So this eliminates half of our initial set of possibilities:

- (1,2,1,1)
- (1,2,2,2)

In bits, it leaves us with 1 bit. Because with 1 binary question (0 or 1, yes or no) we can isolate which sequences belong in our new set.

| Binary Outcome | Sequences |
|---------------|-----------|
| 0 | (1,2,1,1), (1,2,2,2) |
| 1 | (1,4,4,4), (1,1,1,1) |

In our version we have a probability mass reduction of 2.5. Converting this to binary is asking how many "halvings" it took to go from our original distribution 1 to 0.4. In general:

- 1 bit = reduction to 1/2
- 2 bits = reduction to 1/4
- N bits = reduction to 1 / 2^N

So eyeballing it, 2.5 corresponds to a little more than 1 bit. The conversion is done by solving:

$$
2^L = 2.5
$$

$$
L = \log_2(2.5) = 1.32 \text{ bits}
$$

If it was a reduction in half (1 / 0.5 = 2) it would be 1 bit, and it takes a little more than 1 bit because 2.5 > 2.

And in general:

$$
\text{Surprise}(X) = \log_2 \frac{1}{p(X)}
$$

So conceptually surprise represents the amount of shrinkage of our prior probability to our new probability after observing a new event.
The 1 / p is a ratio of our prior (1) to the new event we just saw.

If the event is very unlikely, p is small and it shrinks our distribution by a huge factor, and we call it surprising.

If the event is very likely, p is large and the 1 / p ratio is very small and it shrinks our probability by a small amount.

We take that ratio and apply a logarithm to transform the ratio of shrinkage into the 'number of halvings' our distribution shrunk by after seeing that event P.
The unit becomes bits and 1 bit means we removed half of the uncertainty, 2 bits means 1/4, 3 bits means 1/8, and so on.
Usually we end up somewhere with a fractional bit. In our example of 1.32 the uncertainty was reduced by one full halving plus a little extra because we removed 60% of the probability space (P = 0.40). Which is slightly more then 1 bit or a 50% reduction.

---