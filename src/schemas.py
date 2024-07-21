import datetime

from pydantic import BaseModel

from src.db.models import ZodiacSigns


class GetHoroscopeSchema(BaseModel):
    id: int
    pub_date: datetime.datetime
    zodiac_sign: ZodiacSigns
    horoscope_text: str
