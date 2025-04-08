from dataclasses import dataclass


@dataclass
class TronRecordInfoDTO:
    id: int
    address: str
    create_date: str


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
