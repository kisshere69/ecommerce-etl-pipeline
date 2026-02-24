from extract import extract
from transform import transform
from load import load

RAW_PATH = "data/raw/orders.csv"

def main():
    df = extract(RAW_PATH)
    df_clean = transform(df)
    load(df_clean)
    print("Pipeline executed successfully.")

if __name__ == "__main__":
    main()