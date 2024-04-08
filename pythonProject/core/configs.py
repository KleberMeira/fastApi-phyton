from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """""]
    Configurações gerais
    """
    API_V1_STR: str = '/api/v1'
    BD_URL: str = "postgresql+asyncpg://usuario:senha@localhost:5432/faculdade"
    DBbaseModel = declarative_base()
    ##mudar dps
    JWT_SECRET: str = 'qHKYoRq09AyNPaYtUu6_p--FDpqjWvT5d7T3XD8BQCM'
    ALGORITHM: str = 'HS256'
    # 1 semana em minutos
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True

settings = Settings()