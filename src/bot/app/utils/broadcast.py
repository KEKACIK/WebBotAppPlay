import asyncio
from typing import Union, Optional

from aiogram import exceptions
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup
from loguru import logger

from app import repo
from app.misc import bot


async def send_message(user_id: int,
                       text: Optional[str] = None,
                       photo: Optional[str] = None,
                       caption: Optional[str] = None,
                       reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, None] = None) -> bool:
    try:
        if text:
            await bot.send_message(chat_id=user_id, text=text, reply_markup=reply_markup)
        elif photo:
            await bot.send_photo(chat_id=user_id, caption=caption, photo=photo, reply_markup=reply_markup)
    except exceptions.TelegramAPIError:
        logger.exception(f"Target [ID:{user_id}]: failed")
    else:
        logger.info(f"Target [ID:{user_id}]: success")
        return True
    return False


async def broadcast(text: Optional[str] = None,
                    photo: Optional[str] = None,
                    caption: Optional[str] = None,
                    only_admins: Optional[bool] = False,
                    reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, None] = None) -> int:
    """
    Simple broadcaster
    :return: Count of messages
    """
    count = 0
    try:
        if not only_admins:
            users_id = await repo.user.get_all_chats_id()
        else:
            users_id = await repo.user.get_admin_chats_id()

        for user_id in users_id:
            if await send_message(user_id=user_id, text=text, caption=caption, photo=photo, reply_markup=reply_markup):
                count += 1
            await asyncio.sleep(.05)  # 20 messages per second (Limit: 30 messages per second)
    finally:
        logger.info(f"{count} messages successful sent.")

    return count
