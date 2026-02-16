from collections import Counter
from collections import defaultdict
import random
from typing import DefaultDict, Dict, List, Optional

BigramModel = DefaultDict[str, Counter]

def train_bigrams(sentences: List[List[str]]) -> BigramModel:
    """
    Build next-word counts:
      model[w][next_w] += 1

    Time:  O(total tokens)
    Space: O(number of observed bigrams)
    """
    model: BigramModel = defaultdict(Counter)

    for sent in sentences or []:
        if not sent:
            continue
        for i in range(len(sent) - 1):
            w, nxt = sent[i], sent[i + 1]
            model[w][nxt] += 1

    return model

def most_common_next(w: str, model: BigramModel) -> str:
    """
    Return the most frequent next token after w, else "".
    """
    if not w or w not in model or not model[w]:
        return ""
    # Counter.most_common(1) returns [(word, count)]
    return model[w].most_common(1)[0][0]

def sample_next(w: str, model: BigramModel, rng: Optional[random.Random] = None) -> str:
    """
    Sample next token proportional to observed frequencies, else "".
    """
    if not w or w not in model or not model[w]:
        return ""
    rng = rng or random.Random()

    counter = model[w]
    total = sum(counter.values())
    r = rng.randrange(total)  # integer in [0, total-1]

    cum = 0
    for nxt, c in counter.items():
        cum += c
        if r < cum:
            return nxt

    return ""  # defensive; shouldn't happen
