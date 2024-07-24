import asyncio
import subprocess

from fastapi import FastAPI

from src.api import horoscope_router
from src.db.database import create_tables, drop_tables
from src.broker import broker, daily_task, scheduler


app = FastAPI(title="Horo Scopes")
app.include_router(horoscope_router)


async def main():
    # await drop_tables()
    # await create_tables()
    print("Application startup successfully!")


if __name__ == '__main__':
    asyncio.run(main())
