from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """""]
    Configurações gerais
    """
    API_V1_STR: str = '/api/v1'
    BD_URL: str = "postgresql+asyncpg://usuario:senha@localhost:5432/faculdade"
    DBbaseModel = declarative_base()

    class Config:
        case_sensitive = True

settings = Settings()