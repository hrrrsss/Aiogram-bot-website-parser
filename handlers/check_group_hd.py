from aiogram import Router
from aiogram.types import ChatMemberUpdated

from owner_id.owner_id import OWNER_ID


check_group_router = Router()

active_groups = set()
active_groups.add(-5040734676)


@check_group_router.my_chat_member()
async def on_status_change(event: ChatMemberUpdated):
    chat_id = event.chat.id

    is_admin = getattr(event.new_chat_member, "can_manage_chat", False)

    for owner_id in OWNER_ID:
        if is_admin:
            active_groups.add(chat_id)
            await event.bot.send_message(
                owner_id,
                f"Бот начал работу в группе '{event.chat.title}'"
            )
        else:
            if chat_id in active_groups:
                active_groups.remove(chat_id)
            await event.bot.send_message(
                owner_id,
                f"Бот не может работать в группе '{event.chat.title}', так как не является администратором"
            )