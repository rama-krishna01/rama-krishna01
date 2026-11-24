# RoleReady — Explainable Job Description Skill-Gap Analyzer

RoleReady compares a student's current skills with the skills explicitly mentioned in a job description. It highlights matching skills, missing skills and a practical learning order.

## Why it is different
Many resume tools return a single opaque match score. RoleReady shows the exact skills it detected, the evidence count in the job description, and why each suggested topic is prioritised.

## Features
- Skill extraction from plain-text job descriptions
- Comparison against a user's self-reported skills
- Frequency-based gap prioritisation
- Suggested learning sequence with prerequisite-aware grouping
- Transparent output; no claim that a score predicts hiring success

## Setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
python app.py --skills "Python, C, Git" --job-description "We need Python, SQL, pandas, machine learning, Git and REST API experience."
```

Or pass a text file:
```bash
python app.py --skills "Python, Flutter" --job-file job_description.txt
```

## Important limitations
- Skill detection uses a small, editable vocabulary and keyword matching.
- It does not understand every synonym, measure actual proficiency, or rank candidates.
- Add skills to `SKILL_ALIASES` in `app.py` to extend the vocabulary.
- Use the output as a study guide, not as an automated hiring decision.

## Tech stack
Python (standard library only)
