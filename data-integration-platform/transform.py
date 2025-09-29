# transform.py
"""
Transform module for ETL pipeline.
"""

import logging

def transform_data(df):
    logging.info("Transforming data: adding 'double_value' column.")
    # Example: add a new column with doubled values
    df['double_value'] = df['value'] * 2
    return df
