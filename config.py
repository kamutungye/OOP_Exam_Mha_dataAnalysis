# Global configuration for the MHA data pipeline
import pandas as pd

#DATA_PATH = "sample_data.xlsx"
#DATA_PATH = pd.read_excel("sample_data.xlsx")
DATA_PATH = pd.read_excel(r"D:\Msc. Data Science\CSC8101 - OOP\Exam Project\sample_data.xlsx")
#print(DATA_PATH.info())

# Example endpoint for a DHIS2 server (placeholder)
DHIS2_BASE_URL = "https://hmis.health.go.ug/"
DHIS2_USERNAME = "your_username"
DHIS2_PASSWORD = "your_password"
REPORT_OUTPUT_DIR = "reports/"

#print("Run successfuly")