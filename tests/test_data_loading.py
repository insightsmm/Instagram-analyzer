import pandas as pd
from pathlib import Path

DATA_FILENAME = Path(__file__).resolve().parents[1] / 'data' / 'gdp_data.csv'

def test_data_file_exists():
    assert DATA_FILENAME.exists(), f"Data file {DATA_FILENAME} not found"


def test_load_gdp_data():
    df = pd.read_csv(DATA_FILENAME)
    assert not df.empty, "GDP data should not be empty"
    for col in ['Country Code', '1960', '2022']:
        assert col in df.columns, f"Expected column '{col}' in data"


def test_year_range():
    df = pd.read_csv(DATA_FILENAME)
    year_columns = [int(c) for c in df.columns if c.isdigit()]
    assert min(year_columns) == 1960
    assert max(year_columns) == 2022
