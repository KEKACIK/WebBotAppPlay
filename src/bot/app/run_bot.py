from loguru import logger

from app import misc
from app.bot.handlers import admin_router, menu_router, profile_router, register_router, shop_router, start_router
from db.init_db import init_db
from utils.logger import configure_logger


def setup():
    import app.bot.middlewares.user_manage  # noqa
    misc.dp.include_router(admin_router)
    misc.dp.include_router(start_router)
    misc.dp.include_router(register_router)
    misc.dp.include_router(menu_router)
    misc.dp.include_router(profile_router)
    misc.dp.include_router(shop_router)


async def on_startup():
    configure_logger(True)

    try:
        await init_db()
    except ConnectionRefusedError:
        logger.error("Failed to connect to database ")
        exit(1)

    setup()
    logger.info("Success init")


if __name__ == '__main__':
    misc.dp.startup.register(on_startup)
    misc.dp.run_polling(misc.bot)
