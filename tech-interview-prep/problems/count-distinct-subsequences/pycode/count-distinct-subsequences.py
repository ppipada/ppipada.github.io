def count_distinct_subsequences(s: str, t: str) -> int:
    """
    Count the number of distinct subsequences of s that equal t.

    DP (1D optimization):
    dp[j] = number of ways to match t[:j] using processed prefix of s
    dp[0] = 1 (empty t matches in exactly 1 way)

    For each char in s:
      update dp backwards so we don't reuse the same s-char multiple times.

    Time:  O(len(s) * len(t))
    Space: O(len(t))
    """
    n, m = len(s), len(t)
    if m == 0:
        return 1
    if n == 0:
        return 0

    dp = [0] * (m + 1)
    dp[0] = 1

    for ch in s:
        for j in range(m - 1, -1, -1):
            if ch == t[j]:
                dp[j + 1] += dp[j]

    return dp[m]
