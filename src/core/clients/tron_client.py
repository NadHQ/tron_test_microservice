import asyncio
from concurrent.futures.thread import ThreadPoolExecutor
from functools import partial

from tronpy import Tron
from tronpy.providers import HTTPProvider

from src.config.tron import get_tron_config
from src.tron.dto.tron import TronAccountDTO, TronAddressDTO


class TronClient:
    def __init__(self) -> None:
        self._tron = Tron(
            provider=HTTPProvider(api_key=get_tron_config().TRONGRID_API_KEY)
        )
        self._executor = ThreadPoolExecutor()

    async def get_address_information(self, address: TronAddressDTO) -> TronAccountDTO:
        loop = asyncio.get_event_loop()

        account: dict = await loop.run_in_executor(
            self._executor, partial(self._tron.get_account, address.address)
        )

        resources: dict = await loop.run_in_executor(
            self._executor, partial(self._tron.get_account_resource, address.address)
        )

        return TronAccountDTO(
            address=address.address,
            bandwidth=resources.get("NetLimit", 0),
            energy=resources.get("EnergyLimit", 0),
            trx_balance=account.get("balance", 0),
        )

    def close(self) -> None:
        self._executor.shutdown(wait=True)
