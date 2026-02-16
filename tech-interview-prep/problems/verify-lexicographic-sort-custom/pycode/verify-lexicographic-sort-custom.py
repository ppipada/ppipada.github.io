from typing import Dict, List


def is_sorted_alien(words: List[str], order: List[str]) -> bool:
    """
    Returns True if `words` is sorted under the custom alphabet `order`.

    Time:  O(total characters across comparisons) ~= O(sum(len(words[i])))
    Space: O(|alphabet|)
    """
    if not words:
        return True

    rank: Dict[str, int] = {ch: i for i, ch in enumerate(order)}

    def in_correct_order(a: str, b: str) -> bool:
        # Compare a vs b according to rank
        i = 0
        n, m = len(a), len(b)
        while i < n and i < m:
            ca, cb = a[i], b[i]
            if ca != cb:
                return rank[ca] < rank[cb]
            i += 1
        # All matched up to min length: shorter must come first
        return n <= m

    for i in range(len(words) - 1):
        if not in_correct_order(words[i], words[i + 1]):
            return False
    return True
