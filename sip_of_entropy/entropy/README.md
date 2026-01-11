# Entropy from First Principles
When cross entropy became a popular loss function in deep learning, it was introduced in ML textbooks with very mechanical arguments. The derivation of entropy would introduce a log term because it made taking gradients easier and talk about how logs have nice additive properties. They would sometimes over simplify to the point of being wrong. For example many ML students believe that the KL divergence is a 'distance between two probability distributions' when it is not a distance at all.

To understand what these concepts are actually measuring requires diving into the field of information theory. Hopefully by the end of this section you will understand at the deepest level why concepts from information theory constantly show up in ML and view learning as fundementally a compression problem. Gradients, backprop, and probability are all important. They give you the mechanics of how to train a model. How to do the math. But information theory explains why the math exists at all. It explains why different networks work better at certain problems and give rise to new network architectures.
If gradients, backprop and probabiity are the grammar of the deep learning language, information theory is the resulting literature that arises.





## Table of Contents
### Entropy
We define surprise and entropy and describe the fundmental problem in compression.
1. [Concept and Intuition](docs/01_concept_and_intuition.md)
2. [Kraft Inequality and Prefix Codes](docs/02_kraft_and_prefix_codes.md)
3. [Formalizing Surprise](docs/03_formalizing_surprise.md)
4. [Surprise and Code Length](docs/04_surprise_and_code_length.md)
5. [Entropy from the Binomial Distribution](docs/05_binomial_derivation.md)

### Entropy Between Messages
Extending the definition of entropy to multiple messages as well as multiple distributions. We end
by deriving mutual information an important concept in machine learning that drives feature selection, representation learning, and model interpretation. We visualize it as a special type of KL divergence.

1. [Joint Entropy](docs/06_joint_entropy.md)
2. TODO: Conditional Entropy
3. TODO: Cross Entropy
4. TODO: Entropy Chain RUle
5. TODO: KL Divergence
6. TODO: Mutual Information
7. TODO: Mutual Information as a KL Divergence


 ### Entropy as a limit
 1. TODO: AEP Theorm
 2. TODO: Shannon source coding theorm


  ### Entropy and Learning
  1. TODO: MDL Principle
  2. TODO: Cross Entropy as a Loss Function
  3. TODO: ICA and Mutual Information
  4. TODO: Information Bottleneck Principle
  5. TODO: Variatonal Autoencoders as compression
  6. TODO: Diffusion Models and Entropy
  7. TODO: Convolutions + Downsampling as compression between layers
