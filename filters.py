from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsGroupJoin(BoundFilter):
    key = "is_group_join"

    def __init__(self, is_group_join: bool):
        self.is_group_join = is_group_join

    async def check(self, update: types.ChatMemberUpdated):
        return update.old_chat_member.status in ("kicked", "left") and \
               update.new_chat_member.status in ("member", "administrator") and \
               update.chat.type in ("group", "supergroup")
