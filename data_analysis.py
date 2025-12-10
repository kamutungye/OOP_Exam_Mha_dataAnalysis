#processing/analysis
 # Create automated analytics for MHA reporting.

import pandas as pd

def generate_health_indicators(df: pd.DataFrame) -> dict:
    
    indicators = {}

    indicators["total_screened"] = len(df)
    indicators["tb_positive_rate"] = df["tb_result"].mean()
    indicators["hiv_positive_rate"] = df["hiv_result"].mean()
    indicators["children_under_18"] = (df["age"] < 18).sum()

    # Country-specific breakdowns
    indicators["screened_by_nationality"] = (
        df.groupby("nationality")["passport_number"].count().to_dict()
    )

    # Gender-based prevalence
    indicators["tb_by_gender"] = (
        df.groupby("gender")["tb_result"].mean().to_dict()
    )

    print("[INFO] Analytics generated.")
    return indicators