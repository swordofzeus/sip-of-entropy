# Deriving Entropy

Conceptually, **entropy** is a measure of how much *surprise* or *randomness* exists across a distribution.
It is closely linked to the fields of **probability** and **combinatorics**.
We will derive entropy from a **binomial distribution**, but first describe its uses and conception.

---

## 🧠 Intuition: Compression and Information

Let's say we have a long novel we are trying to **compress** and send over a network.
Compression means not sending every word literally, but **assigning codes** to each word that are shorter representations.

For example, consider this sentence from our novel:

> "I asked for coffee. I took a sip and realized she added maple syrup in my coffee without asking me."

Instead of sending this sentence directly, we can assign **binary codes** to each word and send the codes, along with a dictionary:

| Word | Binary Code |
|------|--------------|
| I | 0 |
| asked | 1 |
| for | 01 |
| coffee | 11 |

This way, the first part of the sentence can be sent as:

```
0 1 01 11
```

instead of “I asked for coffee.”

---

## ⚙️ The Question Shannon Asked

The question Shannon entropy asks is:
**How do we optimally construct this table?**

The first insight you should have is that the codes `0` and `1` are the most *precious* because they are the shortest possible codes.
They take only **one bit** and hold a lot of information (an entire word).

Shannon’s idea is that the **most frequently used words** should be assigned the **shortest bit sequences** for optimal transmission.


# Understanding Entropy Through Word Frequency

To optimally build the coding table, we would start by constructing a **distribution** of how often each word appears.
For the sake of argument, assume our entire vocabulary comes just from this sentence.
Words like **I** and **coffee** would be the most frequent, so they would get the `0` and `1` codings.

---

### ❓ Question

Let’s say **I**, **sugar**, and **coffee** all have the highest frequencies in this novel and appear about 100 times each.
**Which has the highest entropy?**

A natural tendency might be to say **sugar** and **coffee**, since both have five characters while **I** has only one.
So if we were building a compression protocol, it might seem that assigning `0 = sugar` would save more space than assigning `0 = I`.

This is **incorrect** — they all have **equivalent entropy**, because each word’s appearance is treated as a single **event**, and entropy measures the *surprise* of different events, not their textual length.

---

### 🧠 Conceptual Clarification

Information theory is conceptually linked to compression, but it’s an **ideological abstraction** built around the idea of surprise and uncertainty, not literal text length.
In **coding theory** (which deals with actual compression methods such as *Huffman coding*), the *length of words* or tokens does become relevant.
But in **information theory**, we are concerned only with the **probability distribution of events**.

Imagine discovering another page of this novel.
If the words *I*, *coffee*, and *sugar* all have equally high likelihoods of appearing (perhaps it’s a book about a coffee shop), none of them would be surprising.
But if the word *zebra* suddenly appeared — a word that never occurred in the 200 pages we’ve read — that would be **highly surprising**.
Its **information content** would therefore be higher because it was unexpected.

---

### ⚙️ Formalizing “Surprise”

Because we are using **binary coding** (i.e., 0s and 1s) to represent events, we can start formalizing the concept using the **binomial distribution**.
This distribution models a process with two possible outcomes (e.g., True/False or Heads/Tails) where one outcome has probability \( p \) and the other \( 1 - p \).

The probability mass function (PMF) is given by:

$$
P(X = k) = {n \choose k} p^k (1-p)^{n-k}
$$



where:

| Symbol | Meaning |
|---------|----------|
| \( n \) | Number of trials |
| \( x \) | Number of “successes” (e.g., heads) |
| \( p \) | Probability of success |
| \( 1 - p \) | Probability of failure |

---

## Counting Outcomes in a Binary Process

If we flip a coin once, there are **2 possible outcomes**:

| Flip # | Possible Outcomes |
|---------|-------------------|
| 1 | H, T |

If we flip it twice, there are **4 outcomes**:

| Flip # | Possible Outcomes |
|---------|-------------------|
| 2 | HH, HT, TH, TT |

If we flip it three times, there are **8 outcomes**:

| Flip # | Possible Outcomes |
|---------|-------------------|
| 3 | HHH, HHT, HTH, THH, HTT, THT, TTH, TTT |

In general, for a stochastic binary process, there are
\[
2^{n}
\]
possible distinct sequences of outcomes after \(n\) flips.

---

### Grouping by Number of Successes

Instead of listing every sequence, we can group outcomes by how many times a specific event occurs—for example, the number of **heads**.

For one flip:

| # of Heads | Sequences |
|-------------|------------|
| 1 | H |
| 0 | T |

For two flips:

| # of Heads | Sequences |
|-------------|------------|
| 2 | HH |
| 1 | HT, TH |
| 0 | TT |

For three flips:

| # of Heads | Sequences |
|-------------|------------|
| 3 | HHH |
| 2 | HHT, HTH, ... THH |
| 1 | TTH, THT, HTT |
| 0 | TTT |

---

### General Case

In general, the number of distinct sequences that contain exactly \(k\) successes (for example, \(k\) heads) in \(n\) flips is given by the **binomial coefficient**:

$$
 {n \choose k} = n!/(n-k)! * r
$$
### Combining Counts with Probabilities

Now that we know how to count the number of ways \(k\) successes can occur in \(n\) flips,
we also need to account for the **probability** of each outcome.

Let:
- \(p\) = probability of a single **success** (e.g., getting a head),
- \(1 - p\) = probability of a single **failure** (e.g., getting a tail),
- \(k\) = number of successes,
- \(n\) = total number of flips.

Because each coin flip is independent, the probability of any specific sequence with
\(k\) heads and \(n - k\) tails is given by:

\[
p^{k} (1 - p)^{\,n - k}.
\]

This follows from the **Multiplication Rule for Independent Events**,
which states that if two (or more) events occur independently,
the probability of all of them happening together is the product of their individual probabilities.

---

### Why This Makes Sense

Each flip contributes one probability factor:
- for every head → multiply by \(p\),
- for every tail → multiply by \(1 - p\).

So, for example:
- The sequence `HHT` has probability \(p \times p \times (1 - p) = p^2 (1 - p)\).
- The sequence `HTT` has probability \(p \times (1 - p) \times (1 - p) = p (1 - p)^2\).

Every sequence with \(k\) heads and \(n - k\) tails has the same probability \(p^{k}(1 - p)^{n - k}\).
When combined with the number of such sequences, \(\binom{n}{k}\),
this leads to the **binomial distribution**:

$$
P(X = k) = \binom{n}{k} p^{k} (1 - p)^{n - k}
$$



This represents the number of different ways k successes can be arranged among n binary outcomes.


$$
log(P(X = k)) = log({n \choose k} p^k (1-p)^{n-k})
$$


$$
log(P(X = k)) = log({n \choose k}) + log(p^k (1-p)^{n-k})
$$


$$
log(P(X = k)) = log({n \choose k}) + (log(p^k) + log(1-p)^{n-k})
$$

$$
log(P(X = k)) = log({n \choose k}) + (k*log(p) + (n-k)*log(1-p))
$$

$$
log(P(X = k)) = log(n!) - log( (n-k)! * k!) + (k*log(p) + (n-k)*log(1-p))
$$

The next we substitute k = np. np is the expected value of heads or successes we expect to have over a large enough 'infinite' number of trials.

# Why We Substitute k = np

When we flip a coin many times, not every sequence has the same number of heads.
Some sequences have fewer, some have more — but most sequences cluster around the **expected number** of heads, which is: k = np. That value represents the most probable outcome of the binomial distribution — it’s where the probability curve peaks.

---

## Understanding the Typical Region

As the number of flips n increases, the probability of getting a result *too far away* from np
(for example, all tails, or 90% heads instead of 70%) becomes astronomically small.

Almost every realistic sequence you could observe will have a number of heads *very close* to np.
So when we calculate entropy — the **average information content** — we only need to describe what happens around that "typical" region, because that’s where almost all the probability mass lives.

| Term | Meaning |
|------|----------|
| $$n$$ | Number of trials (coin flips) |
| $$p$$ | Probability of a single success (e.g., heads) |
| $$k$$ | Number of successes (heads) |
| $$np$$ | Expected number of successes (the mean of the distribution) |

This is why in entropy derivations, we substitute $$k = np$$ —
it represents the center of all the most likely outcomes.

---

## What “ε” (Epsilon) Means

The symbol **ε** ("epsilon") is a small positive number that defines what we mean by *close* to p.

For example, if p = 0.7 and we choose ε = 0.01, we are talking about all sequences where the observed fraction of heads is between **0.69 and 0.71**. That range is called the **ε-typical region**.
and it shrinks to a small region as N increases. Due to the combinatorial explosion of different possibilities most probability mass is reserved for a tiny few selected outcomes. It can also be explained via the multiplication rule: 70% H flip, rolling 1 tail isnt that hard. if N is 10, rolling 8-10 tails is very unlikely. If N = 100, rolling 80-100 tails is exponentially more unlikely and practically impossible. Which ties into info theory because when it does happen the code for that outcome is very long (high bits). More bits, means more surprise, higher entropy, because we dont expect to transmit it at often (or at all, like 1 million tails)

<div style="display: flex; justify-content: space-around; align-items: center;"> <img src="binomial_growth.png" alt="Binomial growth" style="width: 45%; height: auto;" /> <img src="expected_region.png" alt="Expected region" style="width: 45%; height: auto;" /> </div>


Almost every long sequence will fall inside this region when $$n$$ is large enough.

| Concept | Description |
|----------|--------------|
| ε | Small tolerance that defines what "close to p" means |
| p - ε to p + ε | Range of values for the observed frequency of successes |
| **ε-typical region** | The set of sequences whose observed frequencies lie within that range |

---

## Putting It All Together

| Idea | Explanation |
|------|--------------|
| **1.** k = np | Marks the center of the typical region — the most probable number of successes |
| **2.** **ε defines width** | Sets how far from p we still consider “typical” |
| **3.** **Law of Large Numbers** | As n grows, almost all outcomes lie within that ε-region |
| **4.** **Entropy’s role** | Measures how many bits we need (on average) to describe the typical region |

So:
- Substituting k = np doesn’t ignore other outcomes — it **anchors** the analysis at the region where almost all probability lies.
- The nearby outcomes within p ± ε are automatically accounted for because, as n → ∞, they behave the same way as the mean case.
- Entropy describes the **information rate** of that typical region — the number of bits required to identify one sequence from the many likely ones.



