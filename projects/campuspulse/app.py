"""CampusPulse: demo demand forecasting for a campus canteen."""
from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

DATA = Path(__file__).parent / "data" / "canteen_demand.csv"
NUMERIC = ["temperature_c", "rain_mm", "is_event", "is_exam_period", "is_weekend", "month"]
CATEGORICAL = ["day_of_week"]

def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA, parse_dates=["date"])
    df["day_of_week"] = df["date"].dt.day_name()
    df["month"] = df["date"].dt.month
    return df

def build_model() -> Pipeline:
    prep = ColumnTransformer([
        ("numeric", "passthrough", NUMERIC),
        ("day", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL),
    ])
    return Pipeline([
        ("features", prep),
        ("model", RandomForestRegressor(n_estimators=250, min_samples_leaf=2,
                                         random_state=42, n_jobs=-1)),
    ])

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--predict-date", help="Date in YYYY-MM-DD format")
    parser.add_argument("--rain", type=float, default=0.0, help="Expected rainfall in mm")
    parser.add_argument("--event", type=int, choices=[0, 1], default=0)
    parser.add_argument("--exam", type=int, choices=[0, 1], default=0)
    parser.add_argument("--temperature", type=float, default=28.0)
    args = parser.parse_args()

    df = load_data()
    X = df[NUMERIC + CATEGORICAL]
    y = df["meals_sold"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )
    model = build_model()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("CampusPulse model evaluation (held-out synthetic data)")
    print(f"MAE: {mean_absolute_error(y_test, predictions):.1f} meals")
    print(f"R²:  {r2_score(y_test, predictions):.3f}")
    names = model.named_steps["features"].get_feature_names_out()
    importances = model.named_steps["model"].feature_importances_
    top = sorted(zip(names, importances), key=lambda item: item[1], reverse=True)[:6]
    print("\\nTop demand drivers (feature importance):")
    for name, score in top:
        print(f"  {name}: {score:.3f}")

    if args.predict_date:
        date = pd.Timestamp(args.predict_date)
        row = pd.DataFrame([{
            "temperature_c": args.temperature, "rain_mm": args.rain,
            "is_event": args.event, "is_exam_period": args.exam,
            "is_weekend": int(date.dayofweek >= 5), "month": date.month,
            "day_of_week": date.day_name(),
        }])
        estimate = max(0, round(float(model.predict(row[NUMERIC + CATEGORICAL])[0])))
        print(f"Estimated meals for {date.date()}: {estimate}")

    print("\nReminder: demo data is synthetic; validate on real local data before use.")

if __name__ == "__main__":
    main()
