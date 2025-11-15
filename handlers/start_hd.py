from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from owner_id.owner_id import OWNER_ID


start_router = Router()


@start_router.message(CommandStart())
async def start(message: Message):
    if message.from_user.id in OWNER_ID:
        await message.answer("Добавь меня в группу, чтобы я начал работать.")