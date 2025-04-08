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
    bandwidth: int
    energy: int
    trx_balance: int


@dataclass
class PaginationDTO:
    page: int
    per_page: int
