import pandas as pd


from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:$DB_PASSWORD@localhost:5432/pet_project")
#You need to pass your PostgreSQL password (you can do this manually to test your scripts using this engine)

payments = pd.read_sql("SELECT * FROM payments", engine, parse_dates=["created_at"])