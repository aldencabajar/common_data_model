import os
import pandas as pd
from sqlalchemy import create_engine
from common_data_model.get_query_result import PostgresConfig

cfg = PostgresConfig(
    user=os.getenv('POSTGRES_USER', ''),
    password=os.getenv('POSTGRES_PASSWORD', ''),
    host='localhost',
    db='cdm'
)


engine = create_engine(cfg.url)
db_conn = engine.connect()

query = """
SELECT person_id
FROM cdmschema.person a
"""
df = pd.read_sql(query, con=db_conn)

print(df)
