from dataclasses import dataclass
from typing import List
import pandas as pd
from pandas import DataFrame
from sqlalchemy import create_engine
from common_data_model.config import PostgresConfig


def get_query_result(query: str, config: PostgresConfig) -> DataFrame:
    """get the result from a query string. """

    engine = create_engine(config.url)
    db_conn = engine.connect()
    df = pd.read_sql(query, con=db_conn)
    db_conn.close()
    return df

def get_person(ids: List[int], config: PostgresConfig):
    ...
    """get the result  of person table from CDM."""
    engine = create_engine(config.url)
    db_conn = engine.connect()

    # construct query
    id_list = ','.join([str(i) for i in ids])
    query = f"""
    select * from {config.cdmschema}.person
    where person_id in ({id_list})
    """
    df = pd.read_sql(query, con=db_conn)
    db_conn.close()

    return df