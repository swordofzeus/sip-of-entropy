from entropy import Entropy


class MarginalEntropy(Entropy):
    """Entropy calculations for a marginal (single-variable) distribution."""

    def __init__(self, distribution):
        super().__init__(distribution)

    def surprise(self, event) -> float:
        """Return the surprise of a single event in bits.

        Args:
            event: An outcome from the distribution.
        """
        pass

    def entropy(self) -> float:
        """Return the entropy of the marginal distribution in bits."""
        pass
