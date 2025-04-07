from sqlalchemy.ext.asyncio import AsyncSession


class TronRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, address: str):
        pass

    async def get_records(self, limit: int, offset: int):
        pass
