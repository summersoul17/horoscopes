from typing import AsyncIterator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncEngine

from config import settings

# Создание асинхронного движка БД
async_engine: AsyncEngine = create_async_engine(
    url=settings.DATABASE_URL,
    # echo=True
)

# Создание асинхронной сессии
async_session = async_sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)


async def get_async_session() -> AsyncIterator[AsyncSession]:
    """
    Функция получения асинхронной сессии
    """
    async with async_session() as session:
        yield session
