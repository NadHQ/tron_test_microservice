from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.annotation import Annotated

from src.core.clients.tron_client import TronClient
from src.core.dependencies import get_session, get_tron_client
from src.tron.repositories.tron import TronRepository
from src.tron.services.tron import TronService


def get_tron_repository(
    session: Annotated[AsyncSession, Depends(get_session)]
) -> TronRepository:
    return TronRepository(session)


def get_tron_service(
    tron_repository: Annotated[TronRepository, Depends(get_tron_repository)],
    tron_client: Annotated[TronClient, Depends(get_tron_client)],
) -> TronService:
    return TronService(tron_repository=tron_repository, tron_client=tron_client)
