import asyncio
from pathlib import Path

import structlog
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from structlog.typing import FilteringBoundLogger

from bot.config_reader import bot_config, log_config
from bot.fluent_helper import FluentDispenser
from bot.handlers import commands, pm, add_or_migrate, inline_mode, errors
from bot.logs import get_structlog_config
from bot.middlewares import L10nMiddleware, UnhandledUpdatesLoggerMiddleware
from bot.ui_commands import set_bot_commands

logger: FilteringBoundLogger = structlog.get_logger()


async def main():
    structlog.configure(**get_structlog_config(log_config))

    bot = Bot(
        bot_config.bot_token.get_secret_value(),
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
        )
    )

    # Setup dispatcher and bind routers to it
    dp = Dispatcher()

    dispenser = FluentDispenser(
        locales_dir=Path(__file__).parent.joinpath("locales"),
        default_language="en"
    )
    dp.update.middleware(L10nMiddleware(dispenser))

    if log_config.log_unhandled:
        dp.update.outer_middleware(UnhandledUpdatesLoggerMiddleware())

    # Register handlers
    dp.include_routers(
        commands.router,
        pm.router,
        add_or_migrate.router,
        inline_mode.router,
        errors.router
    )

    # Set bot commands in UI
    await set_bot_commands(bot, dispenser)

    # Run bot
    await logger.awarning("Starting bot")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    await logger.awarning("Bot stopped")


if __name__ == "__main__":
    asyncio.run(main())
