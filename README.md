# sip-of-entropy

[![Release](https://img.shields.io/github/v/release/swordofzeus/sip-of-entropy)](https://img.shields.io/github/v/release/swordofzeus/sip-of-entropy)
[![Build status](https://img.shields.io/github/actions/workflow/status/swordofzeus/sip-of-entropy/main.yml?branch=main)](https://github.com/swordofzeus/sip-of-entropy/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/swordofzeus/sip-of-entropy/branch/main/graph/badge.svg)](https://codecov.io/gh/swordofzeus/sip-of-entropy)
[![Commit activity](https://img.shields.io/github/commit-activity/m/swordofzeus/sip-of-entropy)](https://img.shields.io/github/commit-activity/m/swordofzeus/sip-of-entropy)
[![License](https://img.shields.io/github/license/swordofzeus/sip-of-entropy)](https://img.shields.io/github/license/swordofzeus/sip-of-entropy)

When cross entropy became a popular loss function in deep learning, it was introduced in ML textbooks with very mechanical arguments. The derivation of entropy would introduce a log term because it made taking gradients easier and talk about how logs have nice additive properties. They would sometimes over simplify to the point of being wrong. For example many ML students believe that the KL divergence is a 'distance between two probability distributions' when it is not a distance at all.

To understand what these concepts are actually measuring requires diving into the field of information theory. Hopefully by the end of this section you will understand at the deepest level why concepts from information theory constantly show up in ML and view learning as fundamentally a compression problem. Gradients, backprop, and probability are all important. They give you the mechanics of how to train a model. How to do the math. Information theory explains why the math exists at all. It explains why different networks work better at certain problems and give rise to new network architectures.

If gradients, backprop and probability are the grammar of the deep learning language, information theory is the resulting literature that arises.

- **Github repository**: <https://github.com/swordofzeus/sip-of-entropy/>
- **Documentation**: <https://swordofzeus.github.io/sip-of-entropy/>

---

## Table of Contents

### Entropy
We define surprise and entropy and describe the fundamental problem in compression.
1. [Concept and Intuition](docs/01_concept_and_intuition.md)
2. [Kraft Inequality and Prefix Codes](docs/02_kraft_and_prefix_codes.md)
3. [Formalizing Surprise](docs/03_formalizing_surprise.md)
4. [Surprise and Code Length](docs/04_surprise_and_code_length.md)
5. [Entropy from the Binomial Distribution](docs/05_binomial_derivation.md)

### Entropy Between Messages
Extending the definition of entropy to multiple messages as well as multiple distributions. We end by deriving mutual information — an important concept in machine learning that drives feature selection, representation learning, and model interpretation.

1. [Joint Entropy](docs/06_joint_entropy.md)
2. [Conditional Entropy](docs/07_conditional_entropy.md)
3. TODO: [Slepian–Wolf Theorem](docs/08_slepian_wolf.md)
4. TODO: Cross Entropy
5. TODO: Entropy Chain Rule
6. TODO: KL Divergence
7. TODO: Mutual Information
8. TODO: Mutual Information as a KL Divergence

### Entropy as a Limit
1. TODO: AEP Theorem
2. TODO: Shannon Source Coding Theorem

### Entropy and Learning
1. TODO: Minimum Description Length
2. TODO: Cross Entropy as a Loss Function
3. TODO: ICA and Mutual Information
4. TODO: Information Bottleneck Principle
5. TODO: Variational Autoencoders as Compression
6. TODO: Diffusion Models and Entropy
7. TODO: Convolutions and Downsampling as Lossy Compression

---

## Installation

```bash
make install
```

## Development

```bash
uv run pre-commit run -a
```
