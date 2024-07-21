import json

import aiohttp
import logging

import asyncio

from config import settings

logger = logging.getLogger(__name__)


async def create_vk_post(post_text: str):
    params = {
        'access_token': settings.VK_ACCESS_TOKEN_,
        "v": "5.199",
        'owner_id': settings.VK_OWNER_ID_,
        'from_group': 1,
        "message": post_text,
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(
                'https://api.vk.com/method/wall.post',
                params=params) as response:
            result = await response.text()
            if response.status == 200:
                print("Пост успешно опубликован!", result)
                return True
            else:
                print("Ошибка при создании поста:", result)
                return False
