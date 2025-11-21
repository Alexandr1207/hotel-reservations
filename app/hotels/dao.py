from sqlalchemy import select
from app.dao.base import BaseDAO
from app.hotels.models import Hotels

from app.database import async_session_maker


class HotelDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def find_all(
        cls,
        location: str):
        async with async_session_maker() as session:
            # Правильный SQLAlchemy запрос с ilike для поиска
            query = select(Hotels).where(Hotels.location.ilike(f"%{location}%"))
            result = await session.execute(query)
            return result.scalars().all()