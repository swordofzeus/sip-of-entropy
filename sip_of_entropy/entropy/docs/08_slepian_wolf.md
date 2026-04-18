# Slepian–Wolf Theorem

The Slepian–Wolf theorem is one of the most counterintuitive and beautiful theorems in all of information theory. It shows the limit of compression between two dependent variables.

Suppose we have a joint distribution between two events $(A,B)$. The standard conditional entropy theorem says that if there exists some dependence between $A$ and $B$, i.e., knowing $A$ tells you something about $B$, then the entropy (minimum number of bits) to encode the joint event is less than sending $A$ and $B$ separately.

It says the number of bits is:

$$
H(A,B) = H(A) + H(B|A)
$$

$$
H(A,B) = H(B) + H(A|B)
$$

which is less than the cost of sending $A$ and $B$ separately:

$$
H(A,B) < H(A) + H(B)
$$

---
## Slepian Wolf Setup
Slepian–Wolf takes this a step further.

Imagine instead of a single encoder that sees the joint event, we have two separate encoders $A$ and $B$ that never talk to each other. Each encoder only sees part of the joint event.

- Encoder 1 sees $A$ happened.
- Encoder 2 sees $B$ happened.

Even though the two encoders never talk to each other, Slepian–Wolf says the decoder can still devise an optimal coding scheme that allows it to recover the joint event $(A,B)$ with the same number of bits saved using conditional entropy, despite the encoders never communicating and therefore never observing the event that actually occurred.

In other words, the ability to optimally exploit $A,B$ dependence is so strong that it exists even without the encoders observing the full event. This has huge implications for distributed systems, among other things.

But before you read about how the decoder can recover the full event with fewer bits than sending $H(A) + H(B)$, pause to think about why this could possibly be true. What would a codebook look like?

---

## Example

Imagine we have a weighted deck of cards numbered 1 to 10.

Let:

- A = color (Black or Red)
- B = number (1–10)

Assume the following dependence:

| Color  | Numbers < 5 | Numbers >= 5 |
|---------|-------------|--------------|
| Black   | 70%         | 30%          |
| Red     | 10%         | 90%          |

Now we shuffle the deck and draw a card.

- Encoder 1 sees the color.
- Encoder 2 sees the number.

### Designing an optimal codebook
The distributions suggest an obvious dependence that we can exploit - black cards are much more likely to be smaller and red cards are much likely to be higher. Before diving into the actual codebook used by SW and comparing that to joint entropy. Lets review the standard entropy calculation for this distribution.

#### Standard Entropy (Review)

Entropy is the expectation of surprise over a distribution.
For a random variable \(X\) taking values \(1,2,\dots,10\),

$$
H(X) = \sum_{x=1}^{10} P(x)\,\log\left(\frac{1}{P(x)}\right)
$$

To compute this, we first need the marginal probabilities \(P(x)\).

##### Step 1 — Start from the joint

Each marginal probability is recovered by summing over the joint while holding one variable fixed:

$$
P(x) = P(x,\text{Black}) + P(x,\text{Red})
$$

Using the definition of joint probability,

$$
P(x,\text{Black}) = P(\text{Black})\,P(x \mid \text{Black})
$$

$$
P(x,\text{Red}) = P(\text{Red})\,P(x \mid \text{Red})
$$

So in general,

$$
P(x)
=
P(\text{Black})P(x \mid \text{Black})
+
P(\text{Red})P(x \mid \text{Red})
$$

##### Step 2 — Compute the probabilities

For $x = 1, \dots, 5$, start with the event $X = 1$:

$$
P(X=1)
= P(\text{Black})\cdot\frac{P(\text{low} \mid \text{Black})}{5}
+ P(\text{Red})\cdot\frac{P(\text{low} \mid \text{Red})}{5}
= 0.5\cdot\frac{0.70}{5} + 0.5\cdot\frac{0.10}{5}
$$

The surprise of the event $X = 1$ is:

$$
P(X=1)\,\log\!\left(\frac{1}{P(X=1)}\right)
$$

By symmetry, $P(X=1) = P(X=2) = \cdots = P(X=5)$, so the entropy contribution from the first half is:

$$
\sum_{x=1}^{5} P(X=x)\,\log\!\left(\frac{1}{P(X=x)}\right)
= 5 \cdot P(X=1)\,\log\!\left(\frac{1}{P(X=1)}\right)
= \text{\_\_}\text{ bits}
$$

For $x = 6, \dots, 10$, start with the event $X = 6$:

$$
P(X=6)
= P(\text{Black})\cdot\frac{P(\text{high} \mid \text{Black})}{5}
+ P(\text{Red})\cdot\frac{P(\text{high} \mid \text{Red})}{5}
= 0.5\cdot\frac{0.30}{5} + 0.5\cdot\frac{0.90}{5}
= 0.12
$$

By symmetry, $P(X=6) = P(X=7) = \cdots = P(X=10)$, so the entropy contribution from the second half is:

$$
\sum_{x=6}^{10} P(X=x)\,\log\!\left(\frac{1}{P(X=x)}\right)
= 5 \cdot P(X=6)\,\log\!\left(\frac{1}{P(X=6)}\right)
= 5 \cdot 0.12 \cdot \log_2\!\left(\frac{1}{0.12}\right)
\approx 1.84 \text{ bits}
$$

##### Step 3 — Total entropy of Numerical

$$
H(X) = \sum_{x=1}^{10} P(X=x)\,\log\!\left(\frac{1}{P(X=x)}\right)
= 5 \cdot P(X=1)\,\log_2\!\left(\frac{1}{0.08}\right) + 5 \cdot P(X=6)\,\log_2\!\left(\frac{1}{0.12}\right)
\approx 1.46 + 1.84
= 3.29 \text{ bits}
$$

This means that on average, the number on each card draw requires **3.29 bits** to encode under an optimal code. It is not the cost of any single draw — some outcomes are more surprising and cost more bits, others less — but over many draws, 3.29 bits per draw is the minimum average we can achieve.

##### Step 3 — Total entropy of Color

The color is equally likely to be Black or Red, so:

$$
H(\text{Color}) = 0.5\cdot\log_2\!\left(\frac{1}{0.5}\right) + 0.5\cdot\log_2\!\left(\frac{1}{0.5}\right) = 1 \text{ bit}
$$

##### Step 4 — Total entropy (No Dependence)

Assuming zero dependence, the total bits to encode color and number is simply the sum of their individual entropies:

$$
H(\text{Color}) + H(\text{Number}) = 1 + 3.29 = 4.29 \text{ bits}
$$

##### Step 4 — Total entropy (Exploiting Dependence)
Before we look at how Slepian Wolf comes up with a codebook lets compute the total joint entropy of this distribution. This outlines the theoretical limit a code book could ever do by exploiting the dependent nature between numbers and colors of the cards. It would assign shorter code words to outcomes with much more possible joint outcomes i.e. shorter bit codes to low black cards and higher bit codes to higher number black cards and vice versa for red cards. Your mind should be thinking back to the kraft inequality section and visualizing how the available bit prefix space is optimally partitioned.

Joint Entropy is defined as:
H(A,B) = H(A) + H(B|A)
so we know that H(A) is 1 bit to encode the color. Now we can compute the remaining conditional term to compute the joint entropy across the distribution.


#### Computing the conditional entropy
Before we start chugging away into formulas lets remind ourselves  conditional entropy is measured across an entire distribution. For every possible outcome X, it measures the remaining uncertainity that needs to be filled in for each possible subsequent outcome Y. The first sum is the 'outer loop' of the variable that has already been sent and the inner sum is the expectation of surprise for every remaining outcome.

From the encoders perspective if there is no dependence between any of the events A and B it might as well assign 2 separate codebooks because entropy reduces to H(A) + H(B). However if there is some dependence conditional entropy says instead of having 2 separate codebooks, it can come up with a common scheme where binary codes convey information about events A and B which help reduce the transmission of bits to H(B|A)

Lets start the calculation with a black card. That information is sent through the network and is represented by the $P(X)$ term:

$$
P(X=\text{Black}) \cdot \sum_{y=1}^{10} P(Y=y \mid X=\text{Black})\,\log\!\left(\frac{1}{P(Y=y \mid X=\text{Black})}\right)
$$

Which we can break into two symmetric halves:

$$
P(X=\text{Black})\,\Bigl[\,5 \cdot \text{Surprise}(y \in \{1,\dots,5\}) + 5 \cdot \text{Surprise}(y \in \{6,\dots,10\})\,\Bigr]
$$

Lets take one from each, starting with number being 1 which has a probability of 0.70

| Sample | $P(Y=y \mid \text{Black})$ | Surprise | 5-sequence contribution |
|--------|---------------------------|----------|------------------------|
| $y \in \{1,\dots,5\}$ | $\dfrac{0.70}{5}$ | $\dfrac{0.70}{5}\log\!\left(\dfrac{5}{0.70}\right)$ | $0.70\log\!\left(\dfrac{5}{0.70}\right)$ |
| $y \in \{6,\dots,10\}$ | $\dfrac{0.30}{5}$ | $\dfrac{0.30}{5}\log\!\left(\dfrac{5}{0.30}\right)$ | $0.30\log\!\left(\dfrac{5}{0.30}\right)$ |

The full conditional entropy sums over both colors:

$$
H(Y \mid X) = P(\text{Black})\Bigl[0.70\log\tfrac{5}{0.70} + 0.30\log\tfrac{5}{0.30}\Bigr]
+ P(\text{Red})\Bigl[0.10\log\tfrac{5}{0.10} + 0.90\log\tfrac{5}{0.90}\Bigr]
$$

$$
= 0.5 \times 3.20 + 0.5 \times 2.79 \approx 3.00 \text{ bits}
$$

#### Joint Entropy

| Scheme | Formula | Bits per draw | Bits saved |
|--------|---------|---------------|------------|
| Encode separately (no dependence) | $H(X) + H(Y)$ | 4.29 | — |
| Exploit dependence (joint entropy) | $H(X) + H(Y \mid X)$ | 4.00 | 0.29 |

This is the theoretical limit — no coding scheme can do better than 4.00 bits on average for this distribution.
