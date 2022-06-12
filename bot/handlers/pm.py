from aiogram import Router, types, html, F

router = Router()
router.message.filter(F.chat.type == "private")


@router.message(F.sticker)
async def sticker_in_pm(message: types.Message):
    """
    /start command handler for private chats
    :param message: Telegram message with "/start" command
    """
    await message.reply(
        f"This sticker ID is\n{html.code(message.sticker.file_id)}\n"
        f"Stickers is currently the only media type which file_ids can be used by any bot."
    )


@router.message()
async def other_in_pm(message: types.Message):
    """
    /id command handler for private messages
    :param message: Telegram message with "/id" command
    """
    await message.answer(f"Your Telegram ID is {html.code(message.from_user.id)}")
