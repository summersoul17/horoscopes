import asyncio
import subprocess

import uvicorn
from fastapi import FastAPI

from src.api import horoscope_router
from src.db.database import create_tables, drop_tables
from src.broker import broker, daily_task, scheduler

app = FastAPI(title="Horo Scopes")
app.include_router(horoscope_router)
