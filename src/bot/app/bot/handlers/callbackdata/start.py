from aiogram.dispatcher.filters.callback_data import CallbackData


class GoToCb(CallbackData, prefix="GoTo"):
    action: str


class MainMenuCb(CallbackData, prefix="MainMenu"):
    action: str
