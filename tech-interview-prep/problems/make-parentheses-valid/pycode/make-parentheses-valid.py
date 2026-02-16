from typing import List


def balance_parentheses(s: str) -> str:
    """
    Remove the minimum number of parentheses to make the string valid.

    Approach:
    - Scan once:
      - push indices of '(' onto stack
      - when seeing ')', pop if possible; otherwise mark this ')' as invalid
    - Any remaining '(' in stack are invalid too
    - Build result skipping all invalid indices

    Time:  O(n)
    Space: O(n)
    """
    if not s:
        return ""

    stack: List[int] = []
    invalid = set()

    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                invalid.add(i)

    # Unmatched '(' are invalid
    invalid.update(stack)

    # Rebuild string
    out = []
    for i, ch in enumerate(s):
        if i not in invalid:
            out.append(ch)
    return "".join(out)
