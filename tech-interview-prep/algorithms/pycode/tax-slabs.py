def tax_progressive(income, slabs):
    """
    slabs: list of (lower_inclusive, upper_exclusive_or_None, rate)
    Example:
      slabs = [
        (0, 250000, 0.0),
        (250000, 500000, 0.05),
        (500000, 1000000, 0.20),
        (1000000, None, 0.30),
      ]
    """
    tax = 0.0
    for lo, hi, rate in slabs:
        if income <= lo:
            break
        upper = income if hi is None else min(income, hi)
        taxable = max(0.0, upper - lo)
        tax += taxable * rate
        if hi is not None and income < hi:
            break
    return tax
