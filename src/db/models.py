from datetime import datetime
from sqlalchemy import TIMESTAMP, Text
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from enum import Enum


class Base(DeclarativeBase):
    type_annotation_map = {
        datetime: TIMESTAMP(timezone=True),
    }


class ZodiacSigns(str, Enum):
    ARIES = 'овен'
    TAURUS = 'телец'
    GEMINI = 'близнецы'
    CANCER = 'рак'
    LEO = 'лев'
    VIRGO = 'дева'
    LIBRA = 'весы'
    SCORPIO = 'скорпион'
    SAGITTARIUS = 'стрелец'
    CAPRICORN = 'козерог'
    AQUARIUS = 'водолей'
    PISCES = 'рыбы'


class Horoscope(Base):
    __tablename__ = 'horoscope'

    id: Mapped[int] = mapped_column(primary_key=True)
    pub_date: Mapped[datetime] = mapped_column(default=datetime.utcnow())
    zodiac_sign: Mapped[ZodiacSigns] = mapped_column()
    horoscope_text: Mapped[str] = mapped_column(nullable=False)
