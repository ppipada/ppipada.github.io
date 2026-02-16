def combinations(nums, k):
    """All k-combinations (order doesn't matter)."""
    res = []
    path = []

    def dfs(i):
        if len(path) == k:
            res.append(path.copy())
            return
        if i == len(nums):
            return

        # choose
        path.append(nums[i])
        dfs(i + 1)
        path.pop()

        # skip
        dfs(i + 1)

    dfs(0)
    return res


def combinations_1_to_n(n, k):
    """Classic: choose k numbers from 1..n (pruning)."""
    res = []
    path = []

    def dfs(start):
        if len(path) == k:
            res.append(path.copy())
            return
        # pruning: need (k-len(path)) more numbers
        for x in range(start, n + 1):
            if (n - x + 1) < (k - len(path)):
                break
            path.append(x)
            dfs(x + 1)
            path.pop()

    dfs(1)
    return res
