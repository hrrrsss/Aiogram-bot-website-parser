import asyncio

import logging
from aiogram import Bot

from parsing.third_stage import result_stage_for_aiogram
from common.task_check_sent import check_sent
from lexicon.lexicon import LEXICON


logger = logging.getLogger(__name__)


async def every_hour_task():
    await asyncio.sleep(60)

    while True:
        result_stage_for_aiogram()
        await asyncio.sleep(120)


async def every_20min_task(bot: Bot, chats_id: int):
    await asyncio.sleep(20)

    while True:
        t = check_sent()
        if t:
            for chat_id in chats_id:
                await bot.send_message(chat_id=chat_id, text=LEXICON.format(model=t[1],
                                                                    city=t[2],
                                                                    mileage=t[3],
                                                                    price=t[4],
                                                                    description=t[5],
                                                                    link=t[6],
                                                                    number=t[7]))
                logger.info("Объявление отправленно")
        else:
            logger.info("Пока объявлений нет")

        await asyncio.sleep(15)