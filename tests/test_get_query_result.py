import pytest
from unittest import mock
from common_data_model.get_query_result import get_query_result, get_person
from common_data_model.config import PostgresConfig

@pytest.fixture
def pg_config():
    cfg = PostgresConfig(
        user='foo',
        password='bar',
        host='localhost',
        db='cdm',
        cdmschema='foo'
    )
    return cfg

@mock.patch('common_data_model.get_query_result.create_engine')
@mock.patch('common_data_model.get_query_result.pd')
def test_get_query(pd_mock, create_engine_mock, pg_config):
    query = 'select * from foo'
    get_query_result(query, pg_config)

    create_engine_mock.assert_called_once_with(pg_config.url)

    pd_mock.read_sql.assert_called_once_with(
        query, con=create_engine_mock().connect())


@mock.patch('common_data_model.get_query_result.create_engine')
@mock.patch('common_data_model.get_query_result.pd')
def test_get_person_correct_query(pd_mock, create_engine_mock, pg_config):
    ids = [1,2,3]
    expected_query = f"""
    select * from {pg_config.cdmschema}.person
    where person_id in (1,2,3)
    """

    get_person(ids, pg_config)
    pd_mock.read_sql.assert_called_once_with(
        expected_query,
        con=create_engine_mock().connect()
    )






