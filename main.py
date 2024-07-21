import asyncio
import subprocess
from multiprocessing import Process

from fastapi import FastAPI

from src.api import horoscope_router
from src.broker import broker, daily_task, scheduler
from src.db.database import create_tables

app = FastAPI(title="Horo Scopes")
app.include_router(horoscope_router)


async def run_process(command):
    print(f"[WAIT] Запускаю команду {command}")
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    print(f"[SUCCESS] Запустил команду {command}")
    stdout, stderr = await process.communicate()
    if stdout:
        print(f"Stdout: {stdout.decode()}")
    if stderr:
        print(f"Stderr: {stderr.decode()}")


async def main():
    # await create_tables()
    p1 = Process(target=subprocess.run, args=(["uvicorn", "main:app", "--reload"], ), daemon=True)
    p2 = Process(target=subprocess.run, args=(["taskiq", "scheduler", "main:scheduler"], ), daemon=True)
    p3 = Process(target=subprocess.run, args=(["taskiq", "worker", "main:broker", "main"], ), daemon=True)
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    pass


if __name__ == '__main__':
    asyncio.run(main())
