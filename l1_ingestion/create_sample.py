import pandas as pd
from pathlib import Path


THIS_DIR= Path(__file__).resolve().parent
PROJECT_ROOT = THIS_DIR.parent


RAW_PATH = PROJECT_ROOT/"data/raw/Amazon Sale Report.csv"
SAMPLE_PATH = PROJECT_ROOT/"data/sample/amazon_sample.csv"



df = pd.read_csv(RAW_PATH)
df.head(1000).to_csv(SAMPLE_PATH, index=False)

print("Sample created!")
print(f"Raw file: {RAW_PATH}")
print(f"Sample file: {SAMPLE_PATH}")