from dataclasses import dataclass
from datetime import datetime


@dataclass
class TronRecordInfoDTO:
    id: int
    address: str
    create_date: datetime


@dataclass
class TronAddressDTO:
    address: str


@dataclass
class TronAccountDTO:
    address: str
    bandwidth: float
    energy: float
    trx_balance: float


@dataclass
class PaginationDTO:
    page: int
    per_page: int
