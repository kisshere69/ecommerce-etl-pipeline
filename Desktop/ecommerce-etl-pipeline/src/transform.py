import pandas as pd

def transform(df):

    # Dates
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df = df[df['order_date'].notna()]
    df = df[df['order_date'] <= pd.Timestamp.today()]

    # Remove negative prices
    df = df[df['price'] > 0]

    # Revenue
    df['revenue'] = df['price'] * df['quantity']

    # Country normalization
    df['country'] = df['country'].astype(str).str.strip().str.lower()

    country_map = {
        'lv': 'Latvia',
        'latvia': 'Latvia',
        'germany': 'Germany'
    }

    df['country'] = df['country'].map(country_map)
    df['country'] = df['country'].fillna('Unknown')

    # Remove unknown categories
    df = df[df['product_category'] != 'Unknown']

    print(f"Transformed dataset: {len(df)} rows remaining.")

    return df