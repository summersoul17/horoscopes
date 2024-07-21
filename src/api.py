from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from fastapi import APIRouter, Depends

from src.db.database import get_async_session, async_session
from src.db.models import Horoscope
from src.schemas import GetHoroscopeSchema

horoscope_router = APIRouter(prefix="/horoscope", tags=["horoscope"])


@horoscope_router.get("/", response_model=List[GetHoroscopeSchema], status_code=status.HTTP_200_OK)
async def get_horoscopes(session: AsyncSession = Depends(get_async_session)) -> List[GetHoroscopeSchema]:
    query = select(Horoscope).order_by(Horoscope.pub_date)
    rows = await session.execute(query)
    horoscopes = [GetHoroscopeSchema.model_validate(row) for row in rows.scalars().all()]
    return horoscopes


async def post_horoscope(data: dict):
    async with async_session() as session:
        horoscope = Horoscope(**data)
        session.add(horoscope)
        await session.commit()
