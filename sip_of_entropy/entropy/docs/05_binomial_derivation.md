### ⚙️ Deriving Entropy from the Binomial Distribution 

It is also possible to derive the formula for entropy from a multinomial distribution - in this case we are deriving binary entropy (2 outcomes) for simplicity and using a binomial distribution.
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
- for every head → multiply by p,
- for every tail → multiply by (1 - p).

So, for example:
- The sequence `HHT` has probability p * p * (1 - p) = p^2 (1 - p).
- The sequence `HTT` has probability p * (1 - p) * (1 - p) = p (1 - p)^2.

Every sequence with k heads and n - k tails has the same probability p^{k}(1 - p)^{n - k}.
When combined with the number of such sequences, binom{n}{k},
this leads to the **binomial distribution**:

$$
P(X = k) = \binom{n}{k} p^{k} (1 - p)^{n - k}
$$


## Derivation of Binary Entropy

Start with the combinatorial term:

$$
{n \choose k} = \frac{n!}{k!(n-k)!}
$$

Take the log:

$$
\log {n \choose k} = \log(n!) - \log(k!) - \log((n-k)!)
$$

Apply Stirling’s approximation log(n!) = nlog n - n:

$$
\log {n \choose k} \approx (n\log n - n) - [k\log k - k] - [(n-k)\log(n-k) - (n-k)]
$$

Simplify:

$$
\log {n \choose k} \approx n\log n - k\log k - (n-k)\log(n-k)
$$

Normalize per trial:

$$
\frac{1}{n}\log {n \choose k} \approx \log n - \frac{k}{n}\log k - \left(1 - \frac{k}{n}\right)\log(n-k)
$$

The next step requires substiting k = np.

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

This is why in entropy derivations, we substitute k = np — it represents the center of all the most likely outcomes.

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

## Finsih Entropy Derivation (Substitute k = np)

$$
\frac{1}{n}\log {n \choose np} = \log n - p\log(np) - (1-p)\log(n(1-p))
$$

Expand the log terms:

$$
\log(np) = \log n + \log p, \quad \log(n(1-p)) = \log n + \log(1-p)
$$

Substitute back:

$$
\frac{1}{n}\log {n \choose np} = \log n - [p(\log n + \log p) + (1-p)(\log n + \log(1-p))]
$$

Simplify and cancel \(\log n\) terms:

$$
\frac{1}{n}\log {n \choose np} = -p\log p - (1-p)\log(1-p)
$$

Recognize this as the entropy function:

$$
H(p) = -p\log(p) - (1-p)\log(1-p)
$$


### Summary

| Concept | Meaning |
|----------|----------|
| log(1/p) | Converts probability to "surprise" in bits |
| p log(1/p)| Weights surprise by how often the event occurs |
| H = sum ( p log(1/p) )| Expected surprise (entropy) |
| Fair coin | All outcomes equally surprising (3 bits for 3 flips) |
| Biased coin | Common outcomes use fewer bits; rare ones use more |

Entropy is thus the **theoretical limit of compression** —
the smallest average number of bits required to encode the outcomes of a distribution.