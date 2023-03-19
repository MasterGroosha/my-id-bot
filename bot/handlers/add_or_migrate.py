from asyncio import sleep

from aiogram import types, Bot, html, Router, F
from aiogram.enums import ChatType
from aiogram.filters.chat_member_updated import \
    ChatMemberUpdatedFilter, JOIN_TRANSITION
from fluent.runtime import FluentLocalization

from bot.migration_cache import cache

router = Router()


@router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=JOIN_TRANSITION
    ),
    F.chat.type.in_({ChatType.GROUP, ChatType.SUPERGROUP})
)
async def bot_added_to_group(event: types.ChatMemberUpdated, bot: Bot, l10n: FluentLocalization):
    """
    Bot was added to group.

    :param event: an event from Telegram of type "my_chat_member"
    :param bot: bot who message was addressed to
    :param l10n: Fluent localization object
    :return:
    """
    await sleep(1.0)
    if event.chat.id not in cache.keys():
        await bot.send_message(
            chat_id=event.chat.id,
            text=l10n.format_value(
                msg_id="any-chat",
                args={"type": event.chat.type, "id": html.code(event.chat.id)}
            )
        )


@router.message(F.migrate_to_chat_id)
async def group_to_supergroup_migration(message: types.Message, bot: Bot, l10n: FluentLocalization):
    await bot.send_message(
        message.migrate_to_chat_id,
        l10n.format_value(
            msg_id="group-to-supergroup",
            args={"old_id": html.code(message.chat.id), "new_id": html.code(message.migrate_to_chat_id)}
        )
    )

    cache[message.migrate_to_chat_id] = True
