from typing import Union, List

from aiogram.dispatcher.filters import BaseFilter
from aiogram import types


class ChatTypeFilter(BaseFilter):
    chat_type: Union[str, List[str]]

    async def __call__(self, message: types.Message) -> bool:
        if isinstance(self.chat_type, str):
            return message.chat.type == self.chat_type
        else:
            return message.chat.type in self.chat_type
