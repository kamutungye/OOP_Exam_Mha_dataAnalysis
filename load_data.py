#Load immigration health assessment dataset from CSV or Excel.

import pandas as pd
from config import DATA_PATH

def load_mha_data(path: str = DATA_PATH) -> pd.DataFrame:
    try:
        if not isinstance(path, str):
            raise ValueError(f"Expected file path string, got {type(path)}")

        if path.lower().endswith(".csv"):
            df = pd.read_csv(path)
        else:
            df = pd.read_excel(path)

        print("[INFO] Data loaded successfully.")
        return df

    except Exception as e:
        print(f"[ERROR] Failed to load data: {e}")
        return pd.DataFrame()