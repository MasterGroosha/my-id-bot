from aiogram import Router
from aiogram.exceptions import TelegramAPIError
from aiogram.types import Update

router = Router()


@router.errors()
async def errors_handler(update: Update, exception: TelegramAPIError):
    # Not very good, but for now it's okay
    print(f"{str(exception)}. Update: {update.dict()}")
