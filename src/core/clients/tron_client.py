from concurrent.futures.thread import ThreadPoolExecutor

from tronpy import Tron


class TronClient:
    def __init__(self):
        self._tron = Tron()
        self._executor = ThreadPoolExecutor()

    async def get_address_information(self, address : str):
        pass


    def close(self):
        self._executor.shutdown(wait=True)