from scoring.aps import compute_aps
from scoring.wws import compute_wws
from scoring.ptms import compute_ptms
from scoring.crs import compute_crs
from scoring.sri import compute_sri

student = {
    "attendance": 82,
    "avg_marks": 74,
    "assignment_completion": 90,
    "sleep_hours": 6.5,
    "stress_level": 7,
    "study_hours": 3,
    "deadline_misses": 2,
    "skills_known": ["python","ml"],
    "projects_done": 2,
    "internships": 0,
    "career_clarity": 5
}

aps = compute_aps(
    student["attendance"],
    student["avg_marks"],
    student["assignment_completion"]
)

wws = compute_wws(
    student["sleep_hours"],
    student["stress_level"]
)

ptms = compute_ptms(
    student["study_hours"],
    student["deadline_misses"]
)

crs = compute_crs(
    student["skills_known"],
    student["projects_done"],
    student["internships"],
    student["career_clarity"]
)

sri = compute_sri(aps, wws, ptms, crs)

print(aps, wws, ptms, crs, sri)
