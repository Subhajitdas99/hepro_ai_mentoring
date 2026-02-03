import pandas as pd

from scoring.aps import compute_aps
from scoring.wws import compute_wws
from scoring.ptms import compute_ptms
from scoring.crs import compute_crs
from scoring.sri import compute_sri


def run_scoring():
    df = pd.read_csv("data/raw/students.csv")

    aps, wws, ptms, crs, sri = [], [], [], [], []

    for _, r in df.iterrows():

        aps_val = compute_aps(
            r.gpa,
            r.attendance,
            r.assignments_completion
        )

        wws_val = compute_wws(
            r.stress_level,
            r.sleep_hours,
            r.mental_wellbeing
        )

        ptms_val = compute_ptms(
            r.productivity_score,
            r.distractions,
            r.engagement_score
        )

        crs_val = compute_crs(
            r.skill_readiness,
            r.career_clarity
        )

        sri_val = compute_sri(
            aps_val,
            wws_val,
            ptms_val,
            crs_val
        )

        aps.append(aps_val)
        wws.append(wws_val)
        ptms.append(ptms_val)
        crs.append(crs_val)
        sri.append(sri_val)

    df["APS"] = aps
    df["WWS"] = wws
    df["PTMS"] = ptms
    df["CRS"] = crs
    df["SRI"] = sri

    df.to_csv("data/processed/students_scored.csv", index=False)
    print("✅ students_scored.csv generated")

if __name__ == "__main__":
    run_scoring()

