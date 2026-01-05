# Entropy from First Principles
Since cross entropy became a popular loss function ML textbooks gloss over much of the concepts involving info theory as 'we use logs because they have nice additive properties'. The goal of this section is to conceptually derive every aspect of information theory from scratch starting with concepts progressing into rigerous derivations. It involves stitching together concepts from probability, combinatorics, and coding theory. Hopefully by the end you'll have a deeper and richer understanding of what these concepts are actually measuring. Particularly why these concepts constantly show up in ML theory by understanding learning as fundementally a compression problem.


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

1. TODO: Joint Entropy
2. TODO: Conditional Entropy
3. TODO: Cross Entropy
4. TODO: KL Divergence
5. TODO: Mutual Information
6. TODO: Mutual Information as a KL Divergence
 

 ### Entropy as a limit
 1. TODO: AEP Theorm
 2. TODO: Shannon source coding theorm