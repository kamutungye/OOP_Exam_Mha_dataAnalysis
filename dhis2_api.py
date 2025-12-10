#integration/dhis2
#Mock function for integrating with Uganda national HIS (DHIS2 or similar).

import requests
from requests.auth import HTTPBasicAuth
from config import DHIS2_BASE_URL, DHIS2_USERNAME, DHIS2_PASSWORD

def send_indicator_to_dhis2(indicators: dict):

    endpoint = DHIS2_BASE_URL + "iha-indicators"

    try:
        response = requests.post(
            endpoint,
            json=indicators,
            auth=HTTPBasicAuth(DHIS2_USERNAME, DHIS2_PASSWORD)
        )
        if response.status_code == 200:
            print("[INFO] Indicators successfully sent to DHIS2.")
        else:
            print(f"[ERROR] DHIS2 returned status: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"[ERROR] Failed to send data to DHIS2: {e}")