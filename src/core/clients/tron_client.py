from concurrent.futures.thread import ThreadPoolExecutor

from tronpy import Tron

from src.tron.dto.tron import TronAccountDTO


class TronClient:
    def __init__(self) -> None:
        self._tron = Tron()
        self._executor = ThreadPoolExecutor()

    async def get_address_information(self, address: str) -> TronAccountDTO:
        raise NotImplementedError

    def close(self) -> None:
        self._executor.shutdown(wait=True)
