from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.utils.mappers import orm_to_dto
from src.tron.database.model import TronLogging
from src.tron.dto.tron import TronAccountDTO, TronAddressDTO, TronRecordInfoDTO


class TronRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def add_record(self, tron_address_dto: TronAddressDTO) -> TronRecordInfoDTO:
        record = TronLogging(address=tron_address_dto.address)
        self._session.add(record)
        await self._session.commit()
        await self._session.refresh(record)
        return orm_to_dto(TronRecordInfoDTO, record)

    async def get_records(self, limit: int, offset: int) -> List[TronRecordInfoDTO]:
        stmt = (
            select(TronLogging)
            .order_by(TronLogging.create_date.desc())
            .limit(limit)
            .offset(offset)
        )
        result = await self._session.execute(stmt)
        return [
            orm_to_dto(TronRecordInfoDTO, orm_record)
            for orm_record in result.scalars().all()
        ]
