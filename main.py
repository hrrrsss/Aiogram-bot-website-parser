import asyncio

import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config.config import Config, load_config
from handlers import start_hd, check_group_hd, periodic_tasks
from middlewares.is_admin_mw import AdminCheckMiddleware
from database.connect_db.autokavakaz_con import init_db
from handlers.check_group_hd import active_groups


logger = logging.getLogger(__name__)



async def main():
    config: Config = load_config()

    logging.basicConfig(
        level=logging.getLevelName(level=config.log.level),
        format=config.log.format,
    )
    logger.info("Starting bot")
    
    logger.info("Starting connect db")
    init_db()
    logger.info("DataBase is connect")

    bot = Bot(
        token=config.bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()

    dp.update.middleware(AdminCheckMiddleware())

    dp.include_router(start_hd.start_router)
    dp.include_router(check_group_hd.check_group_router)

    print(active_groups)
    
    asyncio.create_task(periodic_tasks.every_hour_task())
    asyncio.create_task(periodic_tasks.every_20min_task(bot, chats_id=active_groups))


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())