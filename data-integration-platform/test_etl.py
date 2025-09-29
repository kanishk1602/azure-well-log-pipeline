# test_etl.py
import pandas as pd
from extract import extract_data
from transform import transform_data

def test_extract():
    df = extract_data('data/sample.csv')
    assert not df.empty
    assert 'id' in df.columns
    assert 'value' in df.columns

def test_transform():
    df = pd.DataFrame({'id': [1], 'value': [10]})
    df_t = transform_data(df)
    assert 'double_value' in df_t.columns
    assert df_t['double_value'][0] == 20
