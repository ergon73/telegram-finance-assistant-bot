import os
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN", "").strip()
EXCHANGE_RATE_API_KEY = os.getenv("EXCHANGE_RATE_API_KEY", "").strip()

if not TOKEN:
    raise RuntimeError(
        "BOT_TOKEN is not set. Create .env from .env.example and set BOT_TOKEN."
    )

if not EXCHANGE_RATE_API_KEY:
    raise RuntimeError(
        "EXCHANGE_RATE_API_KEY is not set. Create .env from .env.example and set it."
    )

