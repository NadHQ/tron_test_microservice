from pydantic.dataclasses import dataclass


@dataclass
class TronAddressDTO:
    address: str

@dataclass
class TronAccountDTO:
    address: str
    bandwidth: float
    energy: float
    trx_balance: float