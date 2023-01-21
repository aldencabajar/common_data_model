import os
import pandas as pd
from sqlalchemy import create_engine
from common_data_model.config import PostgresConfig

cfg = PostgresConfig(
    user=os.getenv('POSTGRES_USER', ''),
    password=os.getenv('POSTGRES_PASSWORD', ''),
    host='localhost',
    db='cdm',
    cdmschema='cdmschema'
)


engine = create_engine(cfg.url)
db_conn = engine.connect()

query = """
SELECT a.person_id, b.visit_detail_start_date
FROM cdmschema.person a
LEFT JOIN cdmschema.visit_detail b
on a.person_id = b.person_id
where visit_detail_start_date >= '2000-01-01'
"""
df = pd.read_sql(query, con=db_conn)

print(df)
