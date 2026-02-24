from sqlalchemy import create_engine

def load(df):

    engine = create_engine(
        "postgresql+psycopg2://postgres:AdminPassword@localhost:5432/ecommerce"
    )

    df.to_sql(
        "orders_clean",
        engine,
        schema="analytics",
        if_exists="replace",
        index=False
    )

    print("Data loaded into PostgreSQL.")