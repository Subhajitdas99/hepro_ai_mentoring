def compute_aps(attendance, avg_marks, assignment_completion):
    aps = (
        0.3 * attendance +
        0.5 * avg_marks +
        0.2 * assignment_completion
    )
    return round(aps, 2)
