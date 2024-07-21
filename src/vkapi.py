import aiohttp
import logging

from config import settings

logger = logging.getLogger(__name__)


async def create_vk_post(post_text: str):
    params = {
        'access_token': settings.VK_ACCESS_TOKEN_,
        'owner_id': settings.VK_OWNER_ID_,
        'from_group': 1,
        "message": post_text,
        "v": "5.199"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post('https://api.vk.com/method/wall.post', params=params) as response:
            result = await response.json()
            logger.info(f"Пост успешно опубликован! ID поста - {result['response']['post_id']}")
