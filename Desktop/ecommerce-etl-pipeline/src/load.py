import sqlite3

def load(df):
    conn = sqlite3.connect("ecommerce.db")
    df.to_sql("orders", conn, if_exists="replace", index=False)
    conn.close()
    print("Data loaded into SQLite.")