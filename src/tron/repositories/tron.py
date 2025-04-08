from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from src.tron.dto.tron import TronAccountDTO, TronRecordInfoDTO


class TronRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def add_record(self, address: str) -> TronAccountDTO:
        raise NotImplementedError

    async def get_records(self, limit: int, offset: int) -> List[TronRecordInfoDTO]:
        raise NotImplementedError
