from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from src.config.database import get_database_config

config_database = get_database_config()
_AsyncEngine = create_async_engine(
    "postgresql+asyncpg://{user}:{password}@{host}:{port}/{db}".format(
        user=config_database.DATABASE_USER,
        password=config_database.DATABASE_PASSWORD,
        host=config_database.DATABASE_HOST,
        port=config_database.DATABASE_PORT,
        db=config_database.DATABASE_DB,
    )
)

async_session = async_sessionmaker(bind=_AsyncEngine, expire_on_commit=False)
Base = declarative_base()
