import asyncio
from pathlib import Path

from aiogram import Bot, Dispatcher
from fluent.runtime import FluentLocalization, FluentResourceLoader

from bot.config_reader import config
from bot.handlers import commands, pm, add_or_migrate, inline_mode, errors
from bot.ui_commands import set_bot_commands


async def main():
    # Get path to /locales/ dir relative to current file
    locales_dir = Path(__file__).parent.joinpath("locales")
    # Creating Fluent objects
    # FluentResourceLoader uses curly braces, so we cannot use f-strings here
    l10n_loader = FluentResourceLoader(str(locales_dir) + "/{locale}")
    l10n = FluentLocalization(["en"], ["strings.ftl"], l10n_loader)

    bot = Bot(config.bot_token, parse_mode="HTML")

    # Setup dispatcher and bind routers to it
    dp = Dispatcher(l10n=l10n)

    # Register handlers
    dp.include_router(commands.router)
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
