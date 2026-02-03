def compute_wws(stress_level, sleep_hours, mental_wellbeing):
    """
    Wellness & Wellbeing Score (0–100)
    """
    stress_score = (10 - stress_level) * 10        # lower stress = better
    sleep_score = (sleep_hours / 10) * 100         # normalize sleep
    mental_score = mental_wellbeing * 10           # normalize wellbeing

    wws = (
        0.4 * mental_score +
        0.35 * sleep_score +
        0.25 * stress_score
    )

    return round(wws, 2)
