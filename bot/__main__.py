import asyncio

from aiogram import Bot, Dispatcher
from aiogram.dispatcher.router import Router

from bot.config_reader import Config, load_config
from bot.handlers.commands import register_commands
from bot.handlers.forwarded_messages import register_forwards
from bot.handlers.add_or_migrate import register_add_or_migrate
from bot.handlers.inline_mode import register_inline
from bot.handlers.errors import register_errors
from bot.filters.chat_type import ChatTypeFilter
from bot.filters.added_to_group import IsGroupJoin
from bot.ui_commands import set_bot_commands


async def main():
    config: Config = load_config()
    bot = Bot(config.bot.token, parse_mode="HTML")

    # Define the only router
    default_router = Router()

    # Register filters
    default_router.message.bind_filter(ChatTypeFilter)
    default_router.my_chat_member.bind_filter(IsGroupJoin)

    # Register handlers
    register_commands(default_router)
    register_forwards(default_router)
    register_add_or_migrate(default_router)
    register_inline(default_router)
    register_errors(default_router)

    # Setup dispatcher and bind routers to it
    dp = Dispatcher()
    dp.include_router(default_router)

    # Set bot commands in UI
    await set_bot_commands(bot)

    # Run bot
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
