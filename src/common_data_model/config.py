from dataclasses import dataclass

@dataclass
class PostgresConfig:
    user: str
    password: str
    host: str
    db: str
    cdmschema: str

    @property
    def url(self):
        return f'postgresql://{self.user}:{self.password}@{self.host}/{self.db}'
