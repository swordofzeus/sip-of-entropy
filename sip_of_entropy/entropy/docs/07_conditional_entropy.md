# Conditional Entropy

## Joint Distributions (Exercise)

### Pairs of Nucleotides

Imagine an encoder trying to compress the human genome.  
It reads long chunks of codons and assigns shorter codes to sequences it sees more often.

The entropy of a single nucleotide is the weighted sum of surprise over the alphabet:

$$
H(X) = \sum_{x \in \{A, C, T, G\}} P(x)\,\log\frac{1}{P(x)}
$$

Now consider a **joint distribution** over *pairs* of nucleotides.

The possible outcomes are:

| First | Second | Pair |
|-----|------|------|
| A | A | AA |
| A | C | AC |
| A | T | AT |
| A | G | AG |
| C | A | CA |
| ⋮ | ⋮ | ⋮ |
| G | G | GG |

There are 4 * 4 = 16 such outcomes.

The **joint entropy** is defined as:

$$
H(X,Y) = \sum_{x,y} P(x,y)\,\log\frac{1}{P(x,y)}
$$

### Exercise: Is Surprise Additive?

Ask the following question:

> Is the surprise of a pair, for example `AC`, equal to  
> the surprise of `A` plus the surprise of `C`?

In symbols, is the following true?

$$
\text{Surprise}(AC) = \text{Surprise}(A) + \text{Surprise}(C)
$$

If this equality were to hold **for all pairs**, then it would imply:

$$
H(X,Y) = H(X) + H(Y)
$$

The purpose of this example is to pause and think:

- Under what conditions *could* this equality hold?
- Under what conditions *must* it fail?
- What would that imply for compression?

In terms of coding:

- If the equality holds, then encoding pairs offers no advantage over encoding symbols independently.
- If the equality fails, then some pairs may admit shorter codewords than the sum of their individual codes.

---

## Conditional Distributions

In English text, the letter **Q** is almost always followed by the letter **U**
(e.g. *quiz*, *query*, *question*).

Now consider a joint distribution over **pairs of letters** in the alphabet.

- There are 26 letters
- There are 26* 26 = 676 possible pairs

Before considering pairs, look at the **marginal distribution**:

- The letter Q by itself is relatively rare
- The letter U is also not among the most common letters
- Individually, both would receive relatively long codewords

Now suppose the encoder has already transmitted the letter **Q**.

Does it also need to transmit the letter **U**?

In almost all cases, **no**.

The decoder already knows that, given a Q, the next letter is overwhelmingly likely to be U.
The appearance of Q is therefore *highly informative* about the next letter.

This motivates the idea of **conditional entropy**.

---

## Conditional Entropy (Core Idea)

Conditional entropy answers the question:

> Given that event \(X\) has already been observed,  
> how much additional information is required to encode \(Y\)?

Formally, conditional entropy is defined as:

$$
H(Y \mid X) = \sum_x P(x)\,H(Y \mid X=x)
$$

where

$$
H(Y \mid X=x) = \sum_y P(y \mid x)\,\log\frac{1}{P(y \mid x)}
$$

Interpretation:

- If knowing \(X\) tells you **nothing** about \(Y\), then:
  $$
  H(Y \mid X) = H(Y)
  $$
  The variables are independent.

- If knowing \(X\) tells you **everything** about \(Y\), then:
  $$
  H(Y \mid X) = 0
  $$
  No additional information needs to be sent.

- Most real systems lie somewhere in between.

---

## Relationship to Joint Entropy

The fundamental relationship tying everything together is:

$$
H(X,Y) = H(X) + H(Y \mid X)
$$

In words:

- \(H(X)\) is the cost of encoding the first event
- \(H(Y \mid X)\) is the remaining cost once the first event is known
- Their sum is the optimal cost of encoding the joint event

From a compression perspective:

- **Joint entropy** is the optimal code length when encoding \((X,Y)\) together
- **Conditional entropy** is the additional code length required for \(Y\), given that \(X\) has already been transmitted


| Perspective | Question Being Asked | Information-Theoretic Interpretation |
|------------|----------------------|--------------------------------------|
| **Encoder** | If I observe these events together, what is the shortest code I can assign to the pair by exploiting how frequently they co-occur? | Joint coding exploits statistical dependence to reduce average code length below separate encoding. |
| **Decoder** | Once I receive this pair, how much does it collapse the probability distribution I had *before* observing it? | Observing a joint event removes uncertainty by collapsing the prior distribution to a posterior. |
| **Comparison** | Did observing the pair remove uncertainty equal to observing each event separately? | If the events are independent, uncertainty is additive; if they are dependent, redundancy reduces total uncertainty removed. |
