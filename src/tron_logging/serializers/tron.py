from dataclasses import Field
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel

from src.core.serializer import BaseSerializer


class TronCreateSerializer(BaseModel):
    address: Annotated[str, Field(..., description="TRON address")]

class TronBaseSerializer(BaseSerializer):
    address: str
    bandwidth: float
    energy: float
    trx_balance: float

class TronDBRecordSerializer(TronBaseSerializer):
    id: int
    created_at: datetime
