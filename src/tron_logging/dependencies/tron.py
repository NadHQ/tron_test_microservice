from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.dependencies import get_session
from src.tron_logging.database.repositories.tron import TronRepository
from src.tron_logging.services.tron import TronService


def get_tron_repository(session : AsyncSession = Depends(get_session)):
    return TronRepository(session)


def get_tron_service(tron_repository : TronRepository = Depends(get_tron_repository)):
    return TronService(tron_repository)