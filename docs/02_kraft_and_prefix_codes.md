# ⚙️ Kraft–McMillan Inequality

Entropy is the expectation of surprise over a distribution, not a single event. An expectation of a distribution is just the value of an outcome times the probability of that outcome, summed over all outcomes.

$$
\mathbb{E}[f(X)] = \sum_x p(x)\, f(x)
$$

If you wanted to measure the expectation of rolling a fair six-sided die, the expected value would be:

```math
\frac{1}{6}\cdot 1
+ \frac{1}{6}\cdot 2
+ \frac{1}{6}\cdot 3
+ \frac{1}{6}\cdot 4
+ \frac{1}{6}\cdot 5
+ \frac{1}{6}\cdot 6
```

Conceptually this is equivalent to the average: if a die is rolled an infinite number of times, the average of all rolls will converge to this value.

In entropy, the expectation is over a value known as the **surprise**. Since entropy is an expectation, the formula is:

$$
H = \sum_x p(x)\, \text{surprise}(x)
$$

To define surprise formally, we revisit the question of assigning binary codes. Codes must be collision-free — we must know when one message ends and another begins. If we assign:

- `0 = HHHHHH`  
- `10 = HHHHHT`

and we write `010` into the decoder, it cannot determine whether the stream represents `0,1,0` or `0,10`. Therefore, the prefixes of each code must be unique. Visualizing each distinct outcome as a leaf in a binary tree, only **leaf nodes** may be used as codewords. A non-leaf node is a prefix of deeper nodes and would create ambiguity.
<p align="center">
  <div style="display: inline-flex; gap: 20px; align-items: center;">
    <img src="leaf_nodes.png" width="180px">
    <table>
      <tr><th>Code</th><th>Symbol</th></tr>
      <tr><td>00</td><td>A</td></tr>
      <tr><td>01</td><td>B</td></tr>
      <tr><td>10</td><td>C</td></tr>
      <tr><td>11</td><td>D</td></tr>
    </table>
  </div>
</p>



As we construct the binary tree, we reserve more codespace for more frequent events by assigning them leaf nodes that have less depth. In the picture below, we compress a more probable event by giving it the entire left subtree (0.5 codespace), and expand the remaining outcomes by breaking them out as sub-branches of `1`, such as `10` (0.25) and `110` / `111` (0.125 each). The total codespace

$$
0.5 + 0.25 + 0.125 + 0.125
$$

must be **<** 1 to guarantee that the prefix space is non-overlapping. We can choose how many subtrees we make and which codes we assign to them, but the total codespace assigned across all leaves cannot exceed 1.

### Kraft–McMillan Inequality
$$
\sum_{x \in \mathcal{X}} 2^{-\ell(x)} \le 1
$$

The kraft mcmillian inequlity forces a constraint that each code word must be uniquely decoable by not sharing the entire prefix of another code word. The length of the collision free codespace must be less then 1. Each bit breaks a codespace down in intervals of 1/2, which is where the 1/2^n comes from. We can partition the codespace in different ways such as reserving more frequently seen outcomes to shorter code spaces higher up in the tree.

<p align="center">
  <div style="display: inline-flex; gap: 20px; align-items: center;">
    <img src="compressed_tree.png" width="240px">
    <table>
      <tr><th>Code</th><th>Symbol</th></tr>
      <tr><td>00</td><td>A</td></tr>
      <tr><td>01</td><td>B</td></tr>
      <tr><td>10</td><td>C</td></tr>
      <tr><td>11</td><td>D</td></tr>
    </table>
  </div>
</p>

To illustrate, consider a fair coin with equal probability of H and T. In a binary tree, each flip divides the remaining coding space in half:

$$
\frac{1}{2},\; \frac{1}{4},\; \frac{1}{8},\; \frac{1}{16}, \dots
$$

<image placeholder>

In an unfair coin, say \(P(H)=0.90\), we want to reserve 90% of our coding space for outcomes beginning with H and 10% for those beginning with T. This does not form a perfectly regular tree, so it is easier to visualize it as a continuously subdivided interval.

Before any flip:

```
(0.0, 1.0)
```

After the first flip:

```
H : (0.0, 0.90)
T : (0.90, 1.0)
```

After the first flip, 90% of the available codespace is reserved for H and the remaining 10% for T. The encoder can select any number within the interval corresponding to the observed outcome, and the decoder knows which branch occurred.

Now we subdivide again. If the first flip was H, we subdivide only the H-interval:

```
HH : (0.0, 0.81)
HT : (0.81, 0.90)
```

If the first flip was T, we subdivide only the T-interval:

```
TH : (0.90, 0.99)
TT : (0.99, 1.0)
```

<image placeholder>

If we keep doing this for flips 3, 4, 5, 6, ..., the interval corresponding to the observed sequence becomes narrower and narrower. The **surprise** of an event measures how much the remaining interval contracts when that event occurs.

### **Geometric interpretation of surprise**

If the current coding interval has width \(W_{\text{before}}\) and the event has probability \(p(x)\), then after observing that event the interval shrinks to:

$$
W_{\text{after}} = W_{\text{before}} \cdot p(x)
$$

Surprise is the geometric amount by which the interval width contracts when the symbol is observed.

#