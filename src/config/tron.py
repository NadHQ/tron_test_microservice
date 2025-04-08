from functools import lru_cache

from src.config.base import AppBaseConfig


class TronConfig(AppBaseConfig):
    TRONGRID_API_KEY: str


@lru_cache
def get_tron_config() -> TronConfig:
    return TronConfig()
