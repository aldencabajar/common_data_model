from common_data_model.config import PostgresConfig


def test_correct_url():
    cfg = PostgresConfig(
        user='foo',
        password='bar',
        host='localhost',
        db='cdm',
        cdmschema='foo'
    )
    assert cfg.url == 'postgresql://foo:bar@localhost/cdm'