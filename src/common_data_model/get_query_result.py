import os
from dataclasses import dataclass
import psycopg2
from typing import List
import pandas as pd
from pandas import DataFrame
from sqlalchemy import create_engine


@dataclass
class PostgresConfig:
    user: str
    password: str
    host: str
    db: str

    @property
    def url(self):
        return f'postgresql://{self.user}:{self.password}@{self.host}/{self.db}'

def get_query_result(query: str, config: PostgresConfig) -> DataFrame:
    """get the result from a query string. """

    engine = create_engine(config.url)
    db_conn = engine.connect()
    df = pd.read_sql(query, con=db_conn)
    db_conn.close()
    return df

def get_person(ids: List[int]):
    """get the result """
    ...