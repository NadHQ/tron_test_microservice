from functools import lru_cache

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.clients.tron_client import TronClient
from src.core.database import async_session


@lru_cache
def get_tron_client() -> TronClient:
    return TronClient()



async def get_session() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
