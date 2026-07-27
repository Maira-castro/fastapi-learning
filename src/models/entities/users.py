from src.models.setting.metadata import metadata
from sqlalchemy import Table, Column, Integer,String

Users = Table(
    "users", #nome da tabela
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_name", String, nullable=True),
    Column("age", Integer),
    Column("uf", String)
)


