import subprocess
from fastapi import FastAPI

from src.api import horoscope_router
from src.worker import app as celery_app

app = FastAPI(title="Horo Scopes")
app.include_router(horoscope_router)


def main():
    subprocess.run("uvicorn main:app --reload", shell=True)


if __name__ == '__main__':
    celery_app.start()
    main()
