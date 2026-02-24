CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS analytics;

CREATE TABLE IF NOT EXISTS raw.orders_raw (
    order_id TEXT PRIMARY KEY,
    order_date TIMESTAMP,
    customer_id INTEGER,
    product_category TEXT,
    price NUMERIC,
    quantity INTEGER,
    country TEXT
);

CREATE TABLE IF NOT EXISTS analytics.orders_clean (
    order_id TEXT PRIMARY KEY,
    order_date TIMESTAMP,
    customer_id INTEGER,
    product_category TEXT,
    price NUMERIC,
    quantity INTEGER,
    revenue NUMERIC,
    country TEXT
);