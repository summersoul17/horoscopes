import aiohttp
from config import settings


async def generate_horoscope():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key " + settings.YANDEX_API_SECRET,


    }
    prompt = {
        "modelUri": f"gpt://{settings.YANDEX_API_KEY}/yandexgpt/free-tier",

        "messages": [
            {
                "role": "user",
                "text": "Представь, что ты ведущий программы о гороскопах. "
                        "Расскажи гороскоп на сегодня для каждого знака зодиака"
            }
        ]
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(
                url='https://llm.api.cloud.yandex.net/foundationModels/v1/completion',
                headers=headers,
                json=prompt) as resp:
            result = await resp.json()
            return result["result"]["alternatives"][0]["message"]["text"]
