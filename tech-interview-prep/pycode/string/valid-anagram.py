import collections


# Sorting solution
def isAnagram(self, s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


# One liner with using counter
def isAnagramCounter(self, s, t):
    return collections.Counter(s) == collections.Counter(t)


# using dicts
def isAnagramDict(self, s, t):
    dic1, dic2 = [0] * 26, [0] * 26
    for item in s:
        dic1[ord(item) - ord('a')] += 1
    for item in t:
        dic2[ord(item) - ord('a')] += 1
    return dic1 == dic2