# Understanding Entropy

**Entropy** is the foundation of information theory and measures of how much *surprise* or *randomness* exists across a distribution. It is closely linked to the fields of **probability** and **combinatorics** and **coding theory**.

We  slowly derive the formula for entropy conceptually in sections 1-4 and then rigerously via the binomial distribution in section 5 arriving at the same value. First we start purely with an example to illustrate the concept informally.

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