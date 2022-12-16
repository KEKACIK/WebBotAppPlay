from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.bot.handlers.callbackdata.start import GoToCb


def start_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(text="Меню бота", callback_data=GoToCb(action='menu').pack()),
        width=1
    )
    return keyboard.as_markup()
