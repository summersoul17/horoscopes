from typing import AsyncIterator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncEngine

from config import settings
from src.db.models import Horoscope

async_engine: AsyncEngine = create_async_engine(
    url=settings.DATABASE_URL,
    # echo=True
)

async_session = async_sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)


async def get_async_session() -> AsyncIterator[AsyncSession]:
    async with async_session() as session:
        yield session


async def create_tables():
    async with async_engine.begin() as connection:
        await connection.run_sync(Horoscope.metadata.create_all)
        await connection.commit()


async def drop_tables():
    async with async_engine.begin() as connection:
        await connection.run_sync(Horoscope.metadata.drop_all)
        await connection.commit()

