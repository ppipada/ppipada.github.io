from collections import Counter
from typing import List, Sequence, Tuple

Card = Tuple[int, ...]  # e.g. (1,0,1,2)

def is_set(cards: Sequence[Card]) -> bool:
    """
    Check whether exactly 3 cards form a valid Set.

    Condition per attribute i:
      len({c1[i], c2[i], c3[i]}) in {1, 3}

    Time:  O(k)
    Space: O(1)
    """
    if len(cards) != 3:
        return False
    a, b, c = cards
    if len(a) != len(b) or len(b) != len(c):
        return False

    k = len(a)
    for i in range(k):
        vals = {a[i], b[i], c[i]}
        if len(vals) not in (1, 3):
            return False
    return True

def _third_value_mod3(x: int, y: int) -> int:
    """
    Values are in {0,1,2}.
    If x==y then third must be same.
    Else third is the remaining value: 0+1+2 - x - y
    """
    return x if x == y else (3 - x - y)

def find_any_set(cards: List[Card]) -> List[Card]:
    """
    Find any set among the given cards (returns the 3 cards), else [].

    Efficient approach (classic SET trick):
    For any two cards A and B, the required third card C is uniquely determined
    attribute-wise (in mod 3 encoding).

    Handles duplicates by using counts.

    Time:  O(n^2 * k)
    Space: O(n)
    """
    n = len(cards)
    if n < 3:
        return []

    counts = Counter(cards)
    unique = list(counts.keys())
    k = len(unique[0]) if unique else 0
    unique_set = set(unique)

    # Iterate over pairs of unique cards (still fine; counts handle duplicates)
    for i in range(len(unique)):
        for j in range(i, len(unique)):
            a = unique[i]
            b = unique[j]

            need = tuple(_third_value_mod3(a[d], b[d]) for d in range(k))
            if need not in unique_set:
                continue

            # Verify availability of 3 cards considering duplicates
            # Build multiset requirement
            req = Counter([a, b, need])
            ok = True
            for card, r in req.items():
                if counts[card] < r:
                    ok = False
                    break
            if ok and is_set([a, b, need]):
                return [a, b, need]

    return []
