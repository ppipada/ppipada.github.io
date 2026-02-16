from collections import Counter


def permutations(nums):
    """All permutations of distinct items. O(n!)."""
    res = []
    used = [False] * len(nums)
    path = []

    def dfs():
        if len(path) == len(nums):
            res.append(path.copy())
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            dfs()
            path.pop()
            used[i] = False

    dfs()
    return res


def unique_permutations(nums):
    """Permutations with duplicates handled. O(n!) worst-case, prunes duplicates."""
    res = []
    counter = Counter(nums)
    path = []
    n = len(nums)

    def dfs():
        if len(path) == n:
            res.append(path.copy())
            return
        for x in list(counter.keys()):
            if counter[x] == 0:
                continue
            counter[x] -= 1
            path.append(x)
            dfs()
            path.pop()
            counter[x] += 1

    dfs()
    return res
