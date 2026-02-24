# E-commerce ETL Pipeline

## Overview
This project demonstrates a simple ETL pipeline using Python (pandas) and SQL.

## Data Issues Handled
- Missing dates
- Negative prices
- Country normalization
- Unknown categories
- Future dates

## Architecture
Raw CSV → Transform → SQLite → Analytics Queries

## How to Run

1. Install dependencies
   pip install -r requirements.txt

2. Run pipeline
   python src/main.py