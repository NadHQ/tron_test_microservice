import pytest


@pytest.mark.asyncio
async def test_check_address_and_get_records(client):
    address = "TYTest123456"

    # 1. POST /check_address
    response = await client.post("/v1/tron/check_address", json={"address": address})
    assert response.status_code == 200
    data = response.json()

    assert data["address"] == address
    assert isinstance(data["bandwidth"], int)
    assert isinstance(data["energy"], int)
    assert isinstance(data["trx_balance"], int)

    # 2. GET /get_records
    response = await client.get("/v1/tron/get_records?page=1&per_page=5")
    assert response.status_code == 200
    records = response.json()

    assert isinstance(records, list)
    assert any(r["address"] == address for r in records)
