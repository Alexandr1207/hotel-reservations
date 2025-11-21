from fastapi import APIRouter

from app.hotels.dao import HotelDAO


router = APIRouter(prefix="/hotels")

@router.get("")
async def get_hotels(location: str):
    hotels = await HotelDAO.find_all(location)
    return hotels