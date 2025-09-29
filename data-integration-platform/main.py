# main.py
"""
Entry point for the Data Integration Platform.
Simulates ETL pipeline: extract, transform, load.
"""

from extract import extract_data
from transform import transform_data
from load import load_data
import logging

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    logging.info("Starting ETL pipeline...")
    df = extract_data()
    logging.info(f"Extracted data:\n{df}")
    df = transform_data(df)
    logging.info(f"Transformed data:\n{df}")
    load_data(df)
    logging.info("ETL pipeline completed.")

if __name__ == "__main__":
    main()
