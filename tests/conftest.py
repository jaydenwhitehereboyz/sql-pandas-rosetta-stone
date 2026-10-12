import os

import pandas as pd
import pytest
from sqlalchemy import create_engine

DB_URL = (
    f"postgresql+psycopg2://postgres:{os.environ['PG_PASSWORD']}"
    "@localhost:5432/pet_project"
)


@pytest.fixture(scope="session")
def engine():
    return create_engine(DB_URL)


@pytest.fixture(scope="session")
def payments(engine):
    return pd.read_sql("SELECT * FROM payments", engine, parse_dates=["created_at"])


@pytest.fixture(scope="session")
def run_sql(engine):
    def _run(path: str) -> pd.DataFrame:
        with open(path, encoding="utf-8") as f:
            df = pd.read_sql(f.read(), engine)
        # Postgres NUMERIC arrives as Python Decimal (object dtype) -> cast to float
        for col in df.select_dtypes("object"):
            try:
                df[col] = df[col].astype(float)
            except (ValueError, TypeError):
                pass  # text column, keep as is
        return df
    return _run