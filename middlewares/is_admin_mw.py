from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from handlers.check_group_hd import active_groups


class AdminCheckMiddleware(BaseMiddleware):
    async def __call__(
            self, 
            handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        
        if hasattr(event, "chat") and event.chat.type in ("group", "supergroup"):
            if event.chat.id not in active_groups:
                return
            
        return await handler(event, data)