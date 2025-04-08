from datetime import datetime

from src.core.serializer import BaseSerializer


class TronCreateSerializer(BaseSerializer):
    address: str


class TronBaseSerializer(BaseSerializer):
    address: str
    bandwidth: float
    energy: float
    trx_balance: float


class TronDBRecordSerializer(BaseSerializer):
    id: int
    address: str
    created_at: datetime
