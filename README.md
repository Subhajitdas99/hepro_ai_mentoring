# HEPro AI+ – Dedicated Mentoring System for Students

## Overview
This project implements an AI-powered mentoring system using a hybrid approach combining rule-based intelligence and machine learning. The system analyzes student academic performance, wellness, productivity, and career readiness to provide personalized mentoring recommendations.

## Key Features
- Rule-based scoring system (APS, WWS, PTMS, CRS, SRI)
- Student readiness clustering using K-Means
- Mentor–student matching using cosine similarity
- Explainable AI decisions
- Modular Python-first architecture

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn

## Project Structure
data/
raw/
processed/
scoring/
pipeline/
ml_models/
intervention/
main.py


## How to Run
```bash
python data/generate_students.py
python -m pipeline.score_pipeline
python -m ml_models.clustering
python -m ml_models.similarity_matching


Author

Subhajit Das
HEPro AI/ML Internship


---

## 📦 Step 5 — Stage Files

```powershell
git add .
