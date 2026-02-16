import math


class RunningStats:
    """Welford's algorithm: online mean/variance in O(1) memory."""
    def __init__(self):
        self.n = 0
        self.mean = 0.0
        self.M2 = 0.0

    def add(self, x: float):
        self.n += 1
        delta = x - self.mean
        self.mean += delta / self.n
        delta2 = x - self.mean
        self.M2 += delta * delta2

    def variance(self):
        if self.n < 2:
            return 0.0
        return self.M2 / (self.n - 1)  # sample variance

    def stddev(self):
        return math.sqrt(self.variance())
