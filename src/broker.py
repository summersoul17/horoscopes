import logging
from datetime import datetime
from asgiref.sync import async_to_sync
from taskiq import TaskiqScheduler
from taskiq.schedule_sources import LabelScheduleSource
from taskiq_redis import RedisAsyncResultBackend, ListQueueBroker

from src.db.models import ZodiacSigns
from src.generate import generate_horoscope
from src.vkapi import create_vk_post
from src.api import post_horoscope

logger = logging.getLogger(__name__)

redis_async_result = RedisAsyncResultBackend(
    redis_url="redis://localhost:6379"
)

# Or you can use PubSubBroker if you need broadcasting
broker = ListQueueBroker(url="redis://localhost:6379", ).with_result_backend(redis_async_result)

scheduler = TaskiqScheduler(
    broker=broker,
    sources=[LabelScheduleSource(broker)],
)


# @broker.task(schedule=[{"cron": "*/1 * * * *", "args": [1]}])
@broker.task(schedule=[{"cron": "0 10 * * *", "args": [1]}])
async def daily_task(*_, **__):
    print("Зашел в дейли таск")
    text = await generate_horoscope()
    print(f"Сгенерировал гороскоп")
    is_created = await create_vk_post(post_text=text.replace("*", "").replace("\n\n", "\n"))
    if is_created:
        for text, sign in zip(text.split("\n\n")[:12], ZodiacSigns):
            data = {
                "pub_date": datetime.utcnow(),
                "zodiac_sign": sign,
                "horoscope_text": text.replace("*", "")
            }
            await post_horoscope(data)
    else:
        print("Данные не добавлены в базу")
