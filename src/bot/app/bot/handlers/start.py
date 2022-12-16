from aiogram import F, Router
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from loguru import logger

from app import repo
from app.bot.handlers.callbackdata.start import GoToCb
from app.bot.handlers.menu import menu_handler
from app.bot.handlers.register import register_handler

# from app.misc import rcon

start_router = Router()


@start_router.message(commands=["start"], state='*')
async def start_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.delete()
    if await repo.authme.get(message.chat.id):
        await menu_handler(message, state)
    else:
        await register_handler(message, state)


@start_router.callback_query(GoToCb.filter(F.action == 'start'), state='*')
async def go_to_start_handler(call: CallbackQuery, state: FSMContext):
    await start_handler(call.message, state)


@start_router.message(commands=["test"], state='*')
async def test(message: Message, state: FSMContext):
    logger.info(message.text.replace('/test', ''))
    # rcon.send_command(message.args())
