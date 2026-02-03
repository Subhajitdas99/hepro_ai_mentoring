def compute_ptms(productivity_score, distractions, engagement_score):
    """
    Productivity & Time Management Score (0–100)
    """
    productivity_base = productivity_score * 10      # 1–10 → 10–100
    distraction_score = (10 - distractions) * 10     # fewer distractions = better

    ptms = (
        0.4 * productivity_base +
        0.3 * distraction_score +
        0.3 * engagement_score
    )

    return round(ptms, 2)

