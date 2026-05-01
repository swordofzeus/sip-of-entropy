from __future__ import annotations
import numpy as np
from sip_of_entropy.distribution.distribution import Distribution
from sip_of_entropy.entropy.marginal_entropy import MarginalEntropy


class MarginalDistribution(Distribution):
    """A single-variable probability distribution."""

    def __init__(self, outcomes: list, probabilities: np.ndarray):
        super().__init__(outcomes, probabilities)
        self.entropy = MarginalEntropy(self)

    def kl_divergence(self, other: MarginalDistribution):
        pass
