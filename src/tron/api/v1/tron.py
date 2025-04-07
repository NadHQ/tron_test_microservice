from typing import Annotated, List

from fastapi import APIRouter
from fastapi.params import Depends, Query

from src.tron.dependencies.tron import get_tron_service
from src.tron.dto.tron import TronAddressDTO
from src.tron.serializers.tron import (TronBaseSerializer,
                                       TronCreateSerializer,
                                       TronDBRecordSerializer)
from src.tron.services.tron import TronService

tron_router = APIRouter(prefix="/v1/tron")


@tron_router.get("/get_records", response_model=List[TronDBRecordSerializer])
async def get_records(
    tron_service: Annotated[TronService, Depends(get_tron_service)],
    page: Annotated[int, Query(1, ge=1, description="Номер страницы")],
    per_page: Annotated[
        int, Query(10, ge=1, le=100, description="Количество записей на странице")
    ],
) -> List[TronDBRecordSerializer]:
    return await tron_service.get_paginated_records(page, per_page)


@tron_router.post("/check_address", response_model=TronBaseSerializer)
async def check_address(
    address_data: TronCreateSerializer,
    tron_service: Annotated[TronService, Depends(get_tron_service)],
) -> TronBaseSerializer:
    dto = TronAddressDTO(address=address_data.address)
    return await tron_service.get_address_info(dto)
