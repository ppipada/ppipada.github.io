import random


def reservoir_sample(stream, k, rng=random):
    """
    Sample k items uniformly from a stream of unknown length.
    Returns a list of size min(k, n).
    """
    reservoir = []
    for i, x in enumerate(stream, start=1):
        if i <= k:
            reservoir.append(x)
        else:
            j = rng.randint(1, i)
            if j <= k:
                reservoir[j - 1] = x
    return reservoir
