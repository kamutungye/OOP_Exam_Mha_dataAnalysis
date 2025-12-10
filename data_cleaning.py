#processing/Clean and standardize health assessment data.

import pandas as pd

def clean_mha_data(df: pd.DataFrame) -> pd.DataFrame:

    print("Columns BEFORE cleaning:", df.columns.tolist())
    
    # Standardize column names
    #df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    df.columns = df.columns.astype(str).str.strip().str.lower().str.replace(" ", "_")
    print("Columns AFTER cleaning:", df.columns.tolist())

    # Remove duplicates
    df = df.drop_duplicates(subset=["passport_number", "full_name"], keep="last")

    # Handle missing values
    df["age"] = df["age"].fillna(df["age"].median())
    df["gender"] = df["gender"].fillna("Unknown")

    # Convert dates
    date_cols = ["screening_date", "dob"]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    # Normalize disease results
    disease_cols = ["tb_result", "hiv_result"]
    for col in disease_cols:
        df[col] = df[col].str.title().replace({"Positive": 1, "Negative": 0})

    print("[INFO] Data cleaned and standardized.")
    return df