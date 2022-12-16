import hashlib
from contextlib import suppress

from aiogram.exceptions import TelegramAPIError

from app import repo, misc


async def delete_messages(chat_id):
    for message in await repo.deletes.get_all(chat_id=chat_id):
        with suppress(TelegramAPIError):
            await misc.bot.delete_message(chat_id=message.chat_id, message_id=message.message_id)
        await repo.deletes.remove(message.id)


def get_hash(text: str):
    return hashlib.md5(text.encode()).hexdigest()
