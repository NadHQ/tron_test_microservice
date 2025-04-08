from typing import List

from src.core.clients.tron_client import TronClient
from src.tron.dto.tron import (PaginationDTO, TronAccountDTO, TronAddressDTO,
                               TronRecordInfoDTO)
from src.tron.repositories.tron import TronRepository


class TronService:
    def __init__(self, tron_repository: TronRepository, tron_client: TronClient):
        self._tron_repo = tron_repository
        self._tron_client = tron_client

    async def get_address_info(self, address: TronAddressDTO) -> TronAccountDTO:
        database_record = await self._tron_repo.add_record(address)

        tron_address_entity = await self._tron_client.get_address_information(address)
        return tron_address_entity

    async def get_paginated_records(
        self, pagination: PaginationDTO
    ) -> List[TronRecordInfoDTO]:
        offset = (pagination.page - 1) * pagination.per_page
        records_list = await self._tron_repo.get_records(
            limit=pagination.per_page, offset=offset
        )
        return records_list
