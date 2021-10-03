from asyncio import sleep

from aiogram import types, Bot
from aiogram.dispatcher.router import Router
from aiogram.dispatcher.filters.content_types import ContentTypesFilter

from bot.migration_cache import cache


async def bot_added_to_group(event: types.ChatMemberUpdated, bot: Bot):
    await sleep(1.0)
    if event.chat.id not in cache.keys():
        await bot.send_message(event.chat.id, f"This {event.chat.type} chat ID is <code>{event.chat.id}</code>")


async def group_to_supegroup_migration(message: types.Message, bot: Bot):
    await bot.send_message(
        message.migrate_to_chat_id,
        f"Group upgraded to supergroup.\n"
        f"Old ID: <code>{message.chat.id}</code>\n"
        f"New ID: <code>{message.migrate_to_chat_id}</code>"
    )
    cache[message.migrate_to_chat_id] = True


def register_add_or_migrate(router: Router):
    router.message.register(group_to_supegroup_migration, ContentTypesFilter(content_types="migrate_to_chat_id"))
    router.my_chat_member.register(bot_added_to_group, is_added_to_group=True)
