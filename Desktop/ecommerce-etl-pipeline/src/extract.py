import pandas as pd

def extract(path):
    df = pd.read_csv(path)
    print(f"Extracted {len(df)} rows.")
    return df