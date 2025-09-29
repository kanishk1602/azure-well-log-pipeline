# extract.py
"""
Extract module for ETL pipeline.
Simulates data extraction from a CSV file or API.
"""
import pandas as pd
import logging

def extract_data(source='data/sample.csv'):
    logging.info(f"Extracting data from {source}")
    try:
        df = pd.read_csv(source)
        logging.info(f"Extracted {len(df)} rows.")
    except FileNotFoundError:
        logging.warning(f"File {source} not found. Using demo data.")
        df = pd.DataFrame({'id': [1, 2, 3], 'value': [10, 20, 30]})
    return df
