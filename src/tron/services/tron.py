from typing import List

from src.core.clients.tron_client import TronClient
from src.tron.dto.tron import TronAccountDTO, TronAddressDTO
from src.tron.repositories.tron import TronRepository


class TronService:
    def __init__(self, tron_repository: TronRepository, tron_client: TronClient):
        self._tron_repo = tron_repository
        self._tron_client = tron_client

    async def get_address_info(self, address: TronAddressDTO) -> TronAccountDTO:
        raise NotImplementedError

    async def get_paginated_records(
        self, page: int, per_page: int
    ) -> List[TronAccountDTO]:
        raise NotImplementedError
