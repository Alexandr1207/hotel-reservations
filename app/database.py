from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

engine = create_async_engine(settings.DATABASE_URL) # Создаем асинхронный движок и передаем в него ссылку на базу

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False) # Создаем сессию(транзакцию), указываем, что она асинхронная и не истекает при завершении

class Base(DeclarativeBase): # Создаем класс для управления миграциями
    pass