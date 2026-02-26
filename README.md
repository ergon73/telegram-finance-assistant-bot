# Telegram Financial Assistant Bot

Учебный проект Telegram-бота на Python (aiogram) по кейсу «Финансовый
бот‑помощник».

## Возможности

1. **Регистрация пользователя** в базе данных SQLite.
2. **Курс валют** (USD→RUB и EUR→RUB) через ExchangeRate-API.
3. **Советы по экономии** (случайный выбор из списка).
4. **Личные финансы**: ввод 3 категорий расходов и сумм с сохранением
   в SQLite (FSM состояния).

## Технологии

- Python 3.11+
- aiogram 3 (Telegram Bot API)
- SQLite (локальная БД `user.db`)
- python-dotenv (переменные окружения из `.env`)
- requests (HTTP-запросы к ExchangeRate-API)

## Быстрый старт на Windows 11

### 1) Клонирование и окружение

1. Клонируй репозиторий.
2. Открой папку проекта.
3. Создай и активируй виртуальное окружение:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

### 2) Настройка переменных окружения

1. Скопируй `.env.example` в `.env`.
2. Укажи:

   - `BOT_TOKEN` — токен Telegram-бота (получить у @BotFather).
   - `EXCHANGE_RATE_API_KEY` — ключ ExchangeRate-API.

Важно:

1. `.env` не коммитится.
2. `user.db` не коммитится.

### 3) Запуск

```powershell
python bot.py
```

Бот запускается в режиме **long polling** (портов не требуется).

## Как пользоваться

1. Открой чат с ботом и отправь `/start`.
2. Используй кнопки меню:

   1. «Регистрация в телеграм боте»
   2. «Курс валют»
   3. «Советы по экономии»
   4. «Личные финансы»

Для корректной работы финансового блока рекомендуется сначала зарегистрироваться.

## База данных

Файл базы данных: `user.db` (создаётся автоматически).

Таблица: `users`

Поля:

1. `telegram_id` (UNIQUE)
2. `name`
3. `category1`, `category2`, `category3`
4. `expenses1`, `expenses2`, `expenses3`

## Структура проекта

- `bot.py` — логика бота, хэндлеры, FSM, работа с БД.
- `config.py` — загрузка переменных окружения и валидация.
- `requirements.txt` — зависимости.
- `.env.example` — шаблон переменных окружения.
- `.gitignore` — исключения для git.

## Автор

Георгий Белянин (Georgy Belyanin) — [georgy.belyanin@gmail.com][1]

[1]: mailto:georgy.belyanin@gmail.com
