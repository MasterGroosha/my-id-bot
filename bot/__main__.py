import asyncio
from pathlib import Path

from aiogram import Bot, Dispatcher

from bot.config_reader import config
from bot.fluent_helper import FluentDispenser
from bot.handlers import commands, pm, add_or_migrate, inline_mode, errors
from bot.middlewares import L10nMiddleware
from bot.ui_commands import set_bot_commands


async def main():
    bot = Bot(config.bot_token.get_secret_value(), parse_mode="HTML")

    # Setup dispatcher and bind routers to it
    dp = Dispatcher()

    dispenser = FluentDispenser(
        locales_dir=Path(__file__).parent.joinpath("locales"),
        default_language="en"
    )
    dp.update.middleware(L10nMiddleware(dispenser))

    # Register handlers
    dp.include_router(commands.router)
    dp.include_router(pm.router)
    dp.include_router(add_or_migrate.router)
    dp.include_router(inline_mode.router)
    dp.include_router(errors.router)

    # Set bot commands in UI
    await set_bot_commands(bot, dispenser)

    # Run bot
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
