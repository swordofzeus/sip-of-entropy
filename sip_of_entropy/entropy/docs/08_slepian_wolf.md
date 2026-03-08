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

For \(x=1,\dots,5\),

$$
P(x)
=
0.5\cdot\frac{0.70}{5}
+
0.5\cdot\frac{0.10}{5}
$$