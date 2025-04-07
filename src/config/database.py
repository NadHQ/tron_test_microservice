from functools import lru_cache

from src.config.base import AppBaseConfig


class DatabaseConfig(AppBaseConfig):

    DATABASE_USER : str
    DATABASE_PASSWORD : str
    DATABASE_HOST : str
    DATABASE_PORT : str
    DATABASE_DB : str

@lru_cache
def get_database_config() -> DatabaseConfig:
    return DatabaseConfig()