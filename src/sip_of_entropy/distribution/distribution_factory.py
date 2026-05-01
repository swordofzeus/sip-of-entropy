from distribution_type import DistributionType
from marginal_distribution import MarginalDistribution
class DistributionFactory:

    def __init__(self):
        self.mapping = {
            DistributionType.marginal: MarginalDistribution
        }

    def create_distribution(self, distribution_type):
        return self.mapping[distribution_type]()



