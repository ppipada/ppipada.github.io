def is_subsequence(s: str, t: str) -> bool:
    """
    Returns True if t is a subsequence of s.

    Time:  O(len(s))
    Space: O(1)
    """
    i = 0  # pointer in t
    for ch in s:
        if i < len(t) and ch == t[i]:
            i += 1
            if i == len(t):
                return True
    return i == len(t)
