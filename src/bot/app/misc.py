import os
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage

from app.core.config import settings

app_dir: Path = Path(os.getcwd())

bot = Bot(settings.TELEGRAM_BOT_TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
