# Автопостинг в паблике ВК автогенерируемых гороскопов

## Получение токенов
- Получить `VK_ACCESS_TOKEN` можно перейдя по ссылке https://vkhost.github.io/ и там нажав на ***VK ADMIN***. Из адресной строки копируем значение параметра `access_token`.
- Получить `VK_OWNER_ID` можно через VK API, указав ID или домен сообщества.
- Получить `YANDEX_API_KEY` и `YANDEX_API_SECRET` можно по гайду из видео https://youtu.be/PUbJSESAkcM.

## Запуск
- Создайте в корневой папке файл `.env` и перенесите туда все файлы из файла `.env.example`, подставив в переменные свои значения.
- Создайте докер-контейнер командой `docker compose up`.
- Раскомментируйте функцию `create_tables()` в файле `main.py`.
- Выполните следующую команду:
```shell
docker compose up --build
```

## Миграции
- Обновить до последней версии
```shell
alembic upgrade head
```
- Создать новые миграции
```shell
alembic revision --autogenerate -m "your comment"
```
- Сбросить все миграции
```shell
alembic downgrade base
```