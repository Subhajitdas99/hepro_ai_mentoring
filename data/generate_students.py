import os
import random
import pandas as pd

os.makedirs("data/raw", exist_ok=True)

programs = ["B.Tech", "MBA", "B.Sc", "MCA"]

def generate_student(i):
    return {
        "student_id": f"S{i:03d}",
        "age": random.randint(18, 25),
        "program": random.choice(programs),
        "semester": random.randint(1, 8),

        "gpa": round(random.uniform(5.0, 9.5), 2),
        "attendance": random.randint(60, 100),
        "assignments_completion": random.randint(60, 100),

        "stress_level": random.randint(1, 10),
        "sleep_hours": random.randint(4, 9),
        "mental_wellbeing": random.randint(3, 10),

        "productivity_score": random.randint(3, 10),
        "distractions": random.randint(1, 10),

        "career_clarity": random.randint(1, 10),
        "skill_readiness": random.randint(2, 10),

        "engagement_score": random.randint(40, 100)
    }

def generate_dataset(n=500):
    data = [generate_student(i) for i in range(1, n+1)]
    df = pd.DataFrame(data)
    df.to_csv("data/raw/students.csv", index=False)
    print("✅ students.csv created with official HEPro structure")

if __name__ == "__main__":
    generate_dataset(500)

