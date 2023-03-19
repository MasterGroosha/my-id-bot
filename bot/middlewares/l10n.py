from typing import Any, Awaitable, Callable, Dict, Final

from aiogram import BaseMiddleware
from aiogram.enums import ChatType
from aiogram.types import TelegramObject, User, Update

from bot.fluent_helper import FluentDispenser


def is_pm(event: Update) -> bool:
    return \
            (event.message and event.message.chat.type == ChatType.PRIVATE) or \
            (event.inline_query and event.inline_query.chat_type == ChatType.SENDER)


class L10nMiddleware(BaseMiddleware):
    middleware_key: Final[str] = "l10n"

    def __init__(self, dispenser: FluentDispenser):
        self.dispenser = dispenser

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        event: Update
        if is_pm(event):
            user: User = data["event_from_user"]
            data[self.middleware_key] = self.dispenser.get_language(user.language_code)
        else:
            data[self.middleware_key] = self.dispenser.default_locale

        return await handler(event, data)
