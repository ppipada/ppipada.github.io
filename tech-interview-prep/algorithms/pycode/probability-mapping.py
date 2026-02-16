def refine_distribution(coarse_probs, conditional_refinement):
    """
    coarse_probs: dict coarse_outcome -> P(coarse)
    conditional_refinement: dict coarse_outcome -> dict refined_outcome -> P(refined | coarse)

    Returns refined_probs: dict refined_outcome -> P(refined)

    Requires each conditional distribution sums to ~1.
    """
    refined = {}
    for coarse, p_coarse in coarse_probs.items():
        cond = conditional_refinement[coarse]
        for r, p_r_given_c in cond.items():
            refined[r] = refined.get(r, 0.0) + p_coarse * p_r_given_c
    return refined
