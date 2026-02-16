from collections import deque


def sliding_window_max(nums, k):
    """
    Monotonic deque: O(n)
    Returns list of max of each window of size k.
    """
    dq = deque()  # store indices, values decreasing
    out = []
    for i, x in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
