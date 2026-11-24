# CampusPulse — Explainable Campus Canteen Demand Forecaster

CampusPulse estimates how many meals a campus canteen may need to prepare. It combines calendar, weather and event signals to help reduce food waste without running short on meals.

## Why it is different
Instead of a generic house-price dataset, this project models a practical campus operations problem and explains which factors influence demand.

## Features
- Reproducible sample dataset included in `data/canteen_demand.csv`
- Feature engineering for day, weekend, exam period and event status
- Random Forest regression with a held-out evaluation split
- MAE and R² metrics, plus feature-importance output
- Command-line prediction for a new day

## Setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Try a prediction
```bash
python app.py --predict-date 2026-12-02 --rain 0 --event 1 --exam 0 --temperature 28
```

## Dataset
The included data is **synthetic demo data**, not real college records. It is suitable for demonstrating the workflow, not for making real catering decisions.

## Next improvements
- Replace demo data with anonymised real canteen counts
- Compare Random Forest with a seasonal baseline
- Add prediction intervals and a Streamlit dashboard
- Monitor model error over time

## Tech stack
Python, pandas, scikit-learn, NumPy
