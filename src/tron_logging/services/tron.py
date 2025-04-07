from typing import List

from src.tron_logging.database.repositories.tron import TronRepository
from src.tron_logging.dto.tron import TronAddressDTO, TronAccountDTO


class TronService:
    def __init__(self, tron_repository : TronRepository):
        self._tron_repo = tron_repository

    async def get_address_info(self, address : TronAddressDTO) -> TronAccountDTO:
        pass

    async def get_paginated_records(self, page : int, per_page : int) -> List[TronAccountDTO]:
        pass
