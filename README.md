# Common Data Model

This package serves as infrastructure to build necessary artifacts for the postgres server containing Common Data Model Tables and code to query said postgres tables.

## Dependencies
Install at least Docker version 20.10.
## Build Infrastructure
Simply run `docker compose up` to simulate patient-related tables and ETL them to postgres to create Common Data Model tables.

Docker-related code is encapsulated in `infrastructure/`.

## Use CDM package 

Install latest package version using:

```bash
pip install https://github.com/aldencabajar/common_data_model/releases/download/latest/common_data_model-0.1.0-py3-none-any.whl
``` 

Get a `pandas.DataFrame` from a query:
```python
from common_data_model.config import PostgresConfig
from common_data_model.get_query_result import get_query_result 

cfg = PostgresConfig(
    user='user'
    password='password'
    host='localhost',
    db='cdm',
    cdmschema='cdmschema'
)

query = 'SELECT count(*) FROM cdmschema.person'

get_query_result(query, cfg)
```

Get a `pandas.DataFrame` from a list of ids from `person` table:

```python
ids = [1, 2, s3]
get_person(ids, cfg)
```

