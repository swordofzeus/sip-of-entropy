from __future__ import annotations
from abc import ABC
import numpy as np

class Distribution(ABC):
    """Abstract base class for probability distributions.

    Subclasses represent different distribution types (marginal, joint,
    conditional) and must implement all abstract methods.

    Attributes:
        outcomes: Ordered list of possible outcomes (e.g. ["Black", "Red"]).
        probabilities: Probabilities for each outcome, aligned by index with outcomes.
    """

    def __init__(self, outcomes: list, probabilities: np.ndarray):
        """Initialise a distribution.

        Args:
            outcomes: Ordered list of outcome labels.
            probabilities: Numpy array of probabilities, one per outcome.
        """
        self.outcomes = outcomes
        self.probabilities = probabilities

    def entropy(self):
        """Return the entropy of this distribution in bits."""
        pass

    def kl_divergence(self, other: Distribution):
        """Return the KL divergence from this distribution to other.

        Measures information lost when other is used to approximate self.

        Args:
            other: The approximating distribution.
        """
        pass

    def simulate(self, n: int):
        """Draw n independent samples from this distribution.

        Args:
            n: Number of samples to draw.
        """
        pass

    def probability(self, outcome) -> float:
        """Return the probability of a single outcome.

        Args:
            outcome: An element of self.outcomes.
        """
        pass

