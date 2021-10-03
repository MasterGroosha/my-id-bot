from aiogram.dispatcher.filters import BaseFilter
from aiogram.types import (ChatMemberUpdated, ChatMemberMember, ChatMemberAdministrator, ChatMemberBanned,
                           ChatMemberLeft, ChatMemberRestricted)


class IsGroupJoin(BaseFilter):
    is_added_to_group: bool

    async def __call__(self, event: ChatMemberUpdated) -> bool:
        old = event.old_chat_member
        new = event.new_chat_member

        this_is_group = event.chat.type in ("group", "supergroup")

        """
        Previously bot was not in group:
            Either its status was "left" or "banned"
                OR
            It was restricted with "is_member" flag set to False
        """
        bot_was_not_in_group: bool = \
            isinstance(old, (ChatMemberLeft, ChatMemberBanned)) or \
            (isinstance(old, ChatMemberRestricted) and old.is_member is False)

        """
        Bot now in group:
            Either its status is "member" or "administrator" (I guess "owner" is not possible)
                OR
            It is restricted with "is_member" flag set to True
        """
        bot_now_in_group: bool = \
            isinstance(new, (ChatMemberMember, ChatMemberAdministrator)) or \
            (isinstance(old, ChatMemberRestricted) and old.is_member is True)

        return (this_is_group and bot_was_not_in_group and bot_now_in_group) == self.is_added_to_group
