import pytest

from src.tron.dto.tron import TronAddressDTO
from src.tron.repositories.tron import TronRepository


@pytest.mark.asyncio
async def test_repository_save(db_session):
    repo = TronRepository(db_session)

    dto = TronAddressDTO(address="TYUnitTest123")

    saved_dto = await repo.add_record(dto)

    assert saved_dto.id is not None
    assert saved_dto.address == dto.address
