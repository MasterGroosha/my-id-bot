from aiogram.types import Update
from aiogram.exceptions import TelegramAPIError
from aiogram.dispatcher.router import Router


async def errors_handler(update: Update, exception: TelegramAPIError):
    # Not very good, but for now it's okay
    print(f"{str(exception)}. Update: {update.dict()}")


def register_errors(router: Router):
    router.errors.register(errors_handler)
