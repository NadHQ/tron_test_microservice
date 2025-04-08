import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)

from main import app
from src.config.database import get_database_config
from src.core.dependencies import get_tron_client


@pytest.fixture
async def db_session():
    config = get_database_config()

    TEST_DB_URL = f"postgresql+asyncpg://{config.DATABASE_USER}:{config.DATABASE_PASSWORD}@{config.DATABASE_HOST}:{config.DATABASE_PORT}/{config.DATABASE_DB}"
    engine = create_async_engine(TEST_DB_URL, echo=False)
    sessionmaker_ = async_sessionmaker(engine, expire_on_commit=False)

    async with sessionmaker_() as session:
        yield session

    await engine.dispose()


@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


class MockTronClient:
    async def get_address_information(self, dto):
        from src.tron.dto.tron import TronAccountDTO

        return TronAccountDTO(
            address=dto.address, bandwidth=9999.0, energy=8888.0, trx_balance=123.456
        )


@pytest.fixture(autouse=True)
async def override_tron_client():
    app.dependency_overrides[get_tron_client] = lambda: MockTronClient()
    yield
    app.dependency_overrides.clear()
