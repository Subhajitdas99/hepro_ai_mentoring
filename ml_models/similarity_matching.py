import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


STUDENT_PATH = "data/processed/students_clustered.csv"
MENTOR_PATH = "data/raw/mentors.csv"


def load_data():
    students = pd.read_csv(STUDENT_PATH)
    mentors = pd.read_csv(MENTOR_PATH)
    return students, mentors


def identify_primary_need(student):
    scores = {
        "academic": student["APS"],
        "wellness": student["WWS"],
        "productivity": student["PTMS"],
        "career": student["CRS"]
    }
    return min(scores, key=scores.get)


def build_student_vector(student):
    return np.array([
        student["APS"],
        student["WWS"],
        student["PTMS"],
        student["CRS"]
    ])


def build_mentor_vector(mentor, primary_need):
    domain_match = 1 if mentor["domain"] == primary_need else 0

    return np.array([
        domain_match * 100,                 # strong weight
        mentor["experience_level"] * 10,
        mentor["availability"] * 10,
        mentor["feedback_score"] * 20
    ])


def match_student(student, mentors, top_k=2):
    primary_need = identify_primary_need(student)
    student_vec = build_student_vector(student).reshape(1, -1)

    results = []

    for _, mentor in mentors.iterrows():
        mentor_vec = build_mentor_vector(mentor, primary_need).reshape(1, -1)
        similarity = cosine_similarity(student_vec, mentor_vec)[0][0]

        results.append({
            "mentor_id": mentor["mentor_id"],
            "domain": mentor["domain"],
            "similarity_score": round(similarity, 3),
            "reason": f"Primary need: {primary_need}"
        })

    return sorted(results, key=lambda x: x["similarity_score"], reverse=True)[:top_k]


def run_matching(sample_size=5):
    students, mentors = load_data()

    print("\n🎯 Mentor–Student Matching Results\n")

    for _, student in students.head(sample_size).iterrows():
        print(f"Student {student['student_id']} | Cluster {student['cluster_id']} | SRI {round(student['SRI'],2)}")

        matches = match_student(student, mentors)

        for m in matches:
            print(
                f"  → Mentor {m['mentor_id']} ({m['domain']}) | "
                f"Similarity: {m['similarity_score']} | {m['reason']}"
            )
        print("-" * 60)


if __name__ == "__main__":
    run_matching()
