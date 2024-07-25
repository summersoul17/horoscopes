from fastapi import FastAPI

from src.api import horoscope_router
from src.broker import broker, daily_task, scheduler  # необходимые импорты для работы TaskIQ

app = FastAPI(title="Horo Scopes")
app.include_router(horoscope_router)
