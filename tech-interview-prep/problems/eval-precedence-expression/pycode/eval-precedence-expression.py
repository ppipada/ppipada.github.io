def eval_plus_mul(expr: str) -> int:
    """
    Evaluate expression with non-negative integers and operators '+' and '*',
    respecting precedence of '*' over '+'.

    Idea:
    - Keep a running `term` (the current multiplication chain).
    - When we hit '+', we add the finished `term` into `total` and start a new term.
    - When we hit '*', we keep multiplying into the same term.

    Time:  O(n)
    Space: O(1)
    """
    if expr is None:
        return 0

    s = expr.replace(" ", "")
    if not s:
        return 0

    total = 0
    term = 0          # current multiplication term
    num = 0
    op = '+'          # previous operator applied to `num` into `term`

    for i, ch in enumerate(s):
        if ch.isdigit():
            num = num * 10 + (ord(ch) - ord('0'))

        # If operator or end: apply previous op
        if (not ch.isdigit()) or i == len(s) - 1:
            if op == '+':
                # term is complete; push it to total, start new term with num
                total += term
                term = num
            elif op == '*':
                term *= num
            else:
                raise ValueError(f"Unexpected operator: {op}")

            op = ch
            num = 0

    return total + term
