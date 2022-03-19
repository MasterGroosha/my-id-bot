import asyncio

from aiogram import Bot, Dispatcher

from bot.config_reader import config
from bot.filters.added_to_group import IsGroupJoin
from bot.filters.chat_type import ChatTypeFilter
from bot.handlers import commands, forwarded_messages, pm, add_or_migrate, inline_mode, errors
from bot.ui_commands import set_bot_commands


async def main():
    bot = Bot(config.bot_token, parse_mode="HTML")

    # Setup dispatcher and bind routers to it
    dp = Dispatcher()

    # Register filters
    dp.message.bind_filter(ChatTypeFilter)
    dp.my_chat_member.bind_filter(IsGroupJoin)

    # Register handlers
    dp.include_router(commands.router)
    dp.include_router(forwarded_messages.router)
    dp.include_router(pm.router)
    dp.include_router(add_or_migrate.router)
    dp.include_router(inline_mode.router)
    dp.include_router(errors.router)

    # Set bot commands in UI
    await set_bot_commands(bot)

    # Run bot
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
