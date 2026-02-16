import heapq


class RunningMedian:
    """
    Two heaps:
      left: max-heap (store negatives)
      right: min-heap
    """
    def __init__(self):
        self.left = []
        self.right = []

    def add(self, x: float):
        if not self.left or x <= -self.left[0]:
            heapq.heappush(self.left, -x)
        else:
            heapq.heappush(self.right, x)

        # rebalance
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def median(self):
        if not self.left and not self.right:
            return None
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2.0
        return -self.left[0]
