from __future__ import annotations

import argparse
from pathlib import Path
import pandas as pd


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Convert column names to clean snake_case format."""
    cleaned = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )
    df.columns = cleaned
    return df


def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    """Apply standard cleaning steps."""
    df = normalize_columns(df)

    df = df.drop_duplicates().reset_index(drop=True)

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype("string").str.strip()

    return df


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """Create derived columns used in analysis."""

    df["age_group"] = pd.cut(
        df["age"],
        bins=[0, 30, 45, 60, 100],
        labels=["18-30", "30-45", "45-60", "60+"]
    )

    df["stay_category"] = pd.cut(
        df["length_of_stay"],
        bins=[0, 3, 7, 30],
        labels=["Short Stay", "Medium Stay", "Long Stay"]
    )

    def assign_risk(row):
        if row["diabetes"] == "Yes" and row["hypertension"] == "Yes":
            return "High"
        elif row["diabetes"] == "Yes" or row["hypertension"] == "Yes":
            return "Medium"
        else:
            return "Low"

    df["risk_tier"] = df.apply(assign_risk, axis=1)

    df["is_readmitted"] = df["readmitted_30_days"]

    return df


def build_clean_dataset(input_path: Path) -> pd.DataFrame:
    """Load raw data and return cleaned dataset."""
    df = pd.read_csv(input_path)
    df = basic_clean(df)
    df = feature_engineering(df)
    return df


def save_processed(df: pd.DataFrame, output_path: Path) -> None:
    """Save cleaned dataset."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Hospital Readmission ETL Pipeline")

    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Path to raw dataset (data/raw/)"
    )

    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Path to processed dataset (data/processed/)"
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    cleaned_df = build_clean_dataset(args.input)
    save_processed(cleaned_df, args.output)

    print(f"Processed dataset saved to: {args.output}")
    print(f"Rows: {len(cleaned_df)} | Columns: {len(cleaned_df.columns)}")


if __name__ == "__main__":
    main()
