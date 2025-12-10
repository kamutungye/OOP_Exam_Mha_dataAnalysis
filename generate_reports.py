#reporting
#Save computed indicators to a JSON report.

import json
import os
from config import REPORT_OUTPUT_DIR

def save_report(indicators: dict, report_name: str = "mha_report.json"):

    os.makedirs(REPORT_OUTPUT_DIR, exist_ok=True)
    path = os.path.join(REPORT_OUTPUT_DIR, report_name)

    with open(path, "w") as f:
        json.dump(indicators, f, indent=4)

    print(f"[INFO] Report saved: {path}")