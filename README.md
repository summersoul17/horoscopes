# Автопостинг в паблике ВК автогенерируемых гороскопов

## Получение токенов
- Получить `VK_ACCESS_TOKEN` можно перейдя по ссылке https://vkhost.github.io/ и там нажав на ***VK ADMIN***. Из адресной строки копируем значение параметра `access_token`.
- Получить `VK_OWNER_ID` можно через VK API, указав ID или домен сообщества.
- Получить `YANDEX_API_KEY` и `YANDEX_API_SECRET` можно по гайду из видео https://youtu.be/PUbJSESAkcM.

## Запуск
- Создайте в корневой папке файл `.env` и перенесите туда все файлы из файла `.env.example`, подставив в переменные свои значения.
- Создайте докер-контейнер командой `docker compose up`.
- Раскомментируйте функцию `create_tables()` в файле `main.py`.
- Запустите файл `main.py`
- Пропишите в трёх процессах следующие команды:

```shell
uvicorn main:app --reload # Запуск веб-сервера для FastAPI
taskiq scheduler main:sceduler # Создание планировщика задач
taskiq worker main:broker main # Создание брокера задач
```