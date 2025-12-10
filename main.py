#main

from load_data import load_mha_data
from data_cleaning import clean_mha_data
from data_analysis import generate_health_indicators
from generate_reports import save_report
from dhis2_api import send_indicator_to_dhis2


def main():
    print("=== Migration Health Assessment Data Pipeline ===")

    # Step 1: Load data
    df = load_mha_data()

    # Step 2: Clean and process
    df_clean = clean_mha_data(df)

    # Step 3: Generate indicators
    indicators = generate_health_indicators(df_clean)

    # Step 4: Save report
    save_report(indicators)

    # Step 5: Integrate with national HIS
    send_indicator_to_dhis2(indicators)

    print("=== Pipeline complete ===")

if __name__ == "__main__":
    main()