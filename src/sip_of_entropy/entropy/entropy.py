from abc import ABC, abstractmethod


class Entropy(ABC):
    """Abstract base class for entropy calculations.

    All entropy types (marginal, joint, conditional) implement this interface,
    allowing them to be composed into distribution objects uniformly.
    """

    def __init__(self, distribution):
        """Initialise with a distribution to compute entropy over.

        Args:
            distribution: A Distribution instance exposing outcomes and probabilities.
        """
        self.distribution = distribution

    @abstractmethod
    def surprise(self, event) -> float:
        """Return the surprise (self-information) of a single event in bits.

        Args:
            event: An outcome from the distribution.
        """

    @abstractmethod
    def entropy(self) -> float:
        """Return the entropy of the distribution in bits."""
