from fastapi import APIRouter
from fastapi.params import Depends, Query

from src.tron_logging.dependencies.tron import get_tron_service
from src.tron_logging.dto.tron import TronAddressDTO
from src.tron_logging.serializers.tron import TronCreateSerializer
from src.tron_logging.services.tron import TronService

tron_router = APIRouter(prefix="/v1/tron")


@tron_router.get("/get_records")
async def get_records(tron_service: TronService = Depends(get_tron_service),
                      page: int = Query(1, ge=1, description="Номер страницы"),
                      per_page: int = Query(10, ge=1, le=100, description="Количество записей на странице"),
                      ):
    return await tron_service.get_paginated_records(page, per_page)


@tron_router.post("/check_address")
async def check_address(address_data: TronCreateSerializer, tron_service: TronService = Depends(get_tron_service)):
    dto = TronAddressDTO(address=address_data.address)
    return await tron_service.get_address_info(dto.address)
