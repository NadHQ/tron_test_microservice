from datetime import datetime

from pydantic import field_validator

from src.core.serializer import BaseSerializer


class TronCreateSerializer(BaseSerializer):
    address: str

    @field_validator("address")
    @classmethod
    def must_start_with_T(cls, v: str) -> str:
        if not v.startswith("T"):
            raise ValueError("TRON-адрес должен начинаться с 'T'")
        return v


class TronBaseSerializer(BaseSerializer):
    address: str
    bandwidth: int
    energy: int
    trx_balance: int


class TronDBRecordSerializer(BaseSerializer):
    id: int
    address: str
    create_date: datetime
