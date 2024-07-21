import logging
import os
from datetime import datetime
from asgiref.sync import async_to_sync

from src.db.models import ZodiacSigns
from src.generate import generate_horoscope
from src.vkapi import create_vk_post
from src.api import post_horoscope

from celery import Celery
from celery.schedules import crontab

logger = logging.getLogger(__name__)

app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['application/json'],
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TIMEZONE='UTC',
    CELERY_BEAT_SCHEDULE={
        'foo_task': {
            'task': 'tasks.daily_task',
            'schedule': 10,  # run every 10 seconds
        },
    },
)


@app.task(name="generate_horoscope")
def daily_task():
    print("Зашел в дейли таск")
    # text = async_to_sync(generate_horoscope)()
    # async_to_sync(create_vk_post)(post_text=text.replace("*", "").replace("\n\n", "\n"))
    # for text, sign in zip(text.split("\n\n")[:12], ZodiacSigns):
    #     data = {
    #         "pub_date": datetime.utcnow(),
    #         "zodiac_sign": sign,
    #         "horoscope_text": text.replace("*", "")
    #     }
    #     async_to_sync(post_horoscope)(data)
