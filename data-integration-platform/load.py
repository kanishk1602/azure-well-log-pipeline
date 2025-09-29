# load.py
"""
Load module for ETL pipeline.
Loads data into a SQLite database using SQLAlchemy.
"""
from sqlalchemy import create_engine
import logging

def load_data(df, db_url='sqlite:///etl_demo.db'):
    logging.info(f"Loading data to database at {db_url}")
    engine = create_engine(db_url)
    df.to_sql('etl_table', engine, if_exists='replace', index=False)
    logging.info('Data loaded to database.')
