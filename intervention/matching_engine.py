import pandas as pd

# -------------------------------------------------
# Load datasets
# -------------------------------------------------
students = pd.read_csv("data/processed/students_clustered.csv")
mentors = pd.read_csv("data/raw/mentors.csv")

# -------------------------------------------------
# Safety check (prevents silent errors)
# -------------------------------------------------
required_student_cols = ["SRI", "PTMS"]
for col in required_student_cols:
    if col not in students.columns:
        raise Exception(f"❌ Missing column in students file: {col}")

if "domain" not in mentors.columns:
    raise Exception("❌ mentors.csv must contain 'domain' column")

# -------------------------------------------------
# 1️⃣ Create cluster labels automatically
# -------------------------------------------------
def assign_cluster_label(row):
    if row["SRI"] < 55:
        return "At-Risk"
    elif row["PTMS"] < 50:
        return "Productivity Risk"
    elif row["SRI"] > 64:
        return "High Performer"
    else:
        return "Stable"

students["cluster_label"] = students.apply(assign_cluster_label, axis=1)

# -------------------------------------------------
# 2️⃣ Map student mentoring need
# -------------------------------------------------
def get_student_need(label):
    mapping = {
        "At-Risk": "academic",
        "Productivity Risk": "productivity",
        "High Performer": "career",
        "Stable": "wellness"
    }
    return mapping.get(label, "wellness")

students["mentor_need"] = students["cluster_label"].apply(get_student_need)

# -------------------------------------------------
# 3️⃣ Mentor matching logic
# -------------------------------------------------
def match_mentor(need):
    match = mentors[mentors["domain"] == need]
    if not match.empty:
        return match.iloc[0]["mentor_id"]
    # fallback mentor (first row)
    return mentors.iloc[0]["mentor_id"]

students["assigned_mentor"] = students["mentor_need"].apply(match_mentor)

# -------------------------------------------------
# 4️⃣ Intervention recommendation
# -------------------------------------------------
def recommend_intervention(label):
    mapping = {
        "At-Risk": "Academic Intervention",
        "Productivity Risk": "Productivity Coaching",
        "High Performer": "Career Acceleration",
        "Stable": "Regular Mentoring"
    }
    return mapping.get(label, "Regular Mentoring")

students["intervention"] = students["cluster_label"].apply(recommend_intervention)

# -------------------------------------------------
# 5️⃣ High-risk alert simulation
# -------------------------------------------------
students["alert"] = students["SRI"].apply(
    lambda x: "⚠️ HIGH RISK ALERT" if x < 50 else "OK"
)

# 🔥 PROFESSIONAL UPGRADE — Priority column
students["priority"] = students["alert"].apply(
    lambda x: "High" if "HIGH RISK" in x else "Normal"
)

# -------------------------------------------------
# 6️⃣ Save final recommendation table
# -------------------------------------------------
output_path = "data/processed/final_recommendations.csv"
students.to_csv(output_path, index=False)

print("✅ Final recommendation table created.")
print(f"📁 Saved to: {output_path}")


