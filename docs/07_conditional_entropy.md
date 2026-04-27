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

# Conditional Entropy — Step-by-Step Derivation

## Joint Entropy (Reference)

The **joint entropy** of two random variables is defined as:

$$
H(X,Y) = \sum_{x,y} P(x,y)\,\log\frac{1}{P(x,y)}
$$

This measures the average surprise of observing a pair (X,Y).

---

## Conditional Entropy (Core Idea)

Conditional entropy answers the question:

> Given that X has already been observed,  
> how much additional information is required to encode Y?

---

## Step 1 — Probability Identity

We begin with the basic identity:

$$
P(X,Y) = P(X)\,P(Y|X)
$$

This states that the probability of observing two events together can be written as:
- first observing X, and
- then observing the remaining uncertainty in Y given that X is already known

---

## Step 2 — Recall What Entropy Is

Entropy is an **expectation of surprise**.

For a single random variable:

$$
H(X) = \sum_x P(x)\,\log\frac{1}{P(x)}
$$

- P(x): how often the event x occurs  
- log(1 / P(x)): the surprise of that event  
- summing over all x: a weighted average of surprise over the distribution

---

## Step 3 — Change the Experiment

To derive **conditional entropy**, we now consider two random variables, X and Y.

We first write the expectation over the joint experiment, leaving the surprise term unspecified:

$$
\sum_{x,y} P(x,y)\,\text{(surprise)}
$$

Substitute the joint identity:

$$
\sum_{x,y} P(x)\,P(y|x)\,\text{(surprise)}
$$

Rearrange the sums:

$$
\sum_x P(x)\sum_y P(y|x)\,\text{(surprise)}
$$

At this stage:
- no conditional entropy has been defined yet
- we have only rewritten the expectation for a joint draw

---

## Step 4 — Choose the Surprise Term

Since X is already known, the remaining uncertainty is in Y.

The surprise of observing y given x is:
$$
\log\frac{1}{P(y|x)}
$$

Substituting this gives the definition of conditional entropy:

$$
H(Y|X)
= \sum_x P(x)\sum_y P(y|x)\,\log\frac{1}{P(y|x)}
$$

Conceptually - the encoder and decoder both know X happened. That is why the outer term is fixed as P(X). What is the minimum number of bits the encoder needs to send to let the decoder know that Y also happend.


---

## Interpretation

- The outer weight P(x) averages over which context X = x occurs
- The inner sum measures the uncertainty remaining in Y once that context is known
- Conditional entropy is therefore an expectation of conditional surprise

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
| **Encoder** | If I observe these events together, what is the shortest code I can assign to the pair by exploiting how frequently they co-occur? | Joint entropy determines the optimal average code length when encoding the pair as a single message. |
| **Decoder** | After receiving the joint message, how much does my uncertainty collapse compared to receiving the two events as separate messages? | If the events are independent, observing the joint message collapses uncertainty by the same amount as observing both messages separately. |
| **Dependence Test** | Does observing the joint event remove the same uncertainty as observing each event individually? | Independence implies additive surprise: \(H(X,Y)=H(X)+H(Y)\). Dependence implies redundancy, so the joint observation collapses **less** uncertainty than two independent observations. |
