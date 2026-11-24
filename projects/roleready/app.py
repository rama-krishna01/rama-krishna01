"""RoleReady: transparent keyword-based skill-gap analysis for job descriptions."""
from __future__ import annotations
import argparse
from collections import Counter

# Edit or extend aliases as you encounter new tools and technologies.
SKILL_ALIASES = {
    "python": ["python", "python 3"],
    "c": ["c programming", " c language ", "c language"],
    "sql": ["sql", "mysql", "postgresql", "sqlite"],
    "machine learning": ["machine learning", "ml algorithms", "scikit-learn", "sklearn"],
    "deep learning": ["deep learning", "neural networks", "pytorch", "tensorflow"],
    "data analysis": ["data analysis", "data analytics", "pandas", "numpy"],
    "data visualization": ["data visualization", "matplotlib", "seaborn", "power bi", "tableau"],
    "nlp": ["natural language processing", "nlp", "text mining"],
    "git": ["git", "github", "version control"],
    "rest apis": ["rest api", "restful api", "api development"],
    "cloud": ["aws", "azure", "google cloud", "cloud computing"],
    "flutter": ["flutter", "dart"],
    "communication": ["communication skills", "verbal communication"],
    "problem solving": ["problem solving", "analytical thinking"],
}

LEARNING_ORDER = [
    "python", "c", "git", "sql", "data analysis", "data visualization",
    "machine learning", "nlp", "deep learning", "rest apis", "cloud",
    "flutter", "communication", "problem solving",
]

def detect_skills(text: str) -> Counter:
    lower = f" {text.lower()} "
    found = Counter()
    for skill, aliases in SKILL_ALIASES.items():
        hits = sum(lower.count(alias.lower()) for alias in aliases)
        if hits:
            found[skill] = hits
    return found

def normalise_user_skills(raw: str) -> set[str]:
    # Accept canonical names and aliases in a comma-separated list.
    found = set()
    for item in raw.split(","):
        item = item.strip().lower()
        if not item:
            continue
        for skill, aliases in SKILL_ALIASES.items():
            if item == skill or item in [a.strip().lower() for a in aliases]:
                found.add(skill)
    return found

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills", required=True, help='Your skills, comma-separated')
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--job-description", help="Paste the job description")
    source.add_argument("--job-file", help="Read job description from a UTF-8 text file")
    args = parser.parse_args()

    job_text = args.job_description if args.job_description is not None else open(
        args.job_file, encoding="utf-8"
    ).read()
    required = detect_skills(job_text)
    current = normalise_user_skills(args.skills)
    matched = sorted(set(required) & current)
    missing = set(required) - current
    priority = sorted(missing, key=lambda skill: (-required[skill],
                     LEARNING_ORDER.index(skill) if skill in LEARNING_ORDER else 999))

    print("\nROLE READY | SKILL GAP REPORT")
    print("=" * 34)
    print(f"Skills detected in description: {len(required)}")
    print(f"Your matched skills: {len(matched)}")
    print(f"Skills to work on: {len(missing)}")

    print("\nMATCHED")
    for skill in matched:
        print(f"  [✓] {skill} (mentioned {required[skill]} time(s))")
    print("\nPRIORITISED SKILL GAPS")
    for index, skill in enumerate(priority, 1):
        print(f"  {index}. {skill} — mentioned {required[skill]} time(s)")
    if not required:
        print("\nNo supported skills were detected. Extend SKILL_ALIASES or check the job text.")
    print("\nThis is a keyword-based study aid, not a hiring score or proficiency test.")

if __name__ == "__main__":
    main()
