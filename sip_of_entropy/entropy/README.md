# Entropy from First Principles

Despite being the foundational concept that underlies information theory, entropy is often presented as a formula to memorize.
This part of the repo devotes 6 sections to understanding what entropy actually measures. It starts from a pure conceptual view with no formulas and slowly builds up the formula from intuition by connecting concepts from probability, combinatorics, and coding theory together. The final section is a purely rigerous mathemtcal derivation from the binomial theorm and it matches the formula we construct in sections 1-5 from a conceptual framework.

Unfortunately since cross entropy became a popular loss function ML textbooks gloss over much of the concepts as 'we use logs because they have nice additive properties'. Hopefully the reader will have a much greater depth of understanding of what these concepts are actually measuring and why they constantly show up in ML theory after reading this section.

## Table of Contents

1. [Concept and Intuition](docs/01_concept_and_intuition.md)
2. [Kraft Inequality and Prefix Codes](docs/02_kraft_and_prefix_codes.md)
3. [Formalizing Surprise](docs/03_formalizing_surprise.md)
4. [Surprise and Code Length](docs/04_surprise_and_code_length.md)
5. [Entropy from the Binomial Distribution](docs/05_binomial_derivation.md)
