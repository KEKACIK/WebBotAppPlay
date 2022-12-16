from typing import Callable, Dict, Any, Awaitable
from typing import Union

from aiogram.types import Message, CallbackQuery
from aiogram.types import Update
from loguru import logger

from app import repo
from app.misc import dp


async def update_user(update: Union[Message, CallbackQuery]):
    user = await repo.user.get(update.from_user.id)
    update_data = {}
    if user:
        if user.username != update.from_user.username:
            update_data["username"] = update.from_user.username

        if update_data:
            await repo.user.update(db_obj=user, **update_data)
    else:
        user = await repo.user.create(id=update.from_user.id, username=update.from_user.username)
    authme = await repo.authme.get(update.from_user.id)
    if authme:
        if not await repo.iconomy.get(authme.id):
            await repo.iconomy.create(id=authme.id, username=authme.realname, balance=0)
        if not await repo.kekastats.get(authme.id):
            await repo.kekastats.create(id=authme.id, username=authme.realname)
    return user


@dp.update.outer_middleware()
async def BigBro(handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]], event: Update, data: Dict[str, Any]) -> Any:
    await update_user(event.message or event.callback_query)
    return await handler(event, data)
