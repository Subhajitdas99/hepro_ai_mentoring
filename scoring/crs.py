def compute_crs(skill_readiness, career_clarity):
    """
    Career Readiness Score (0–100)
    """
    crs = (
        0.6 * (skill_readiness * 10) +
        0.4 * (career_clarity * 10)
    )
    return round(crs, 2)

