from aiogram import Router, types, html, F
from aiogram.enums import ChatType

from aiogram.filters import MagicData

from fluent.runtime import FluentLocalization

router = Router()
router.message.filter(F.chat.type == ChatType.PRIVATE)


@router.message(F.forward_from_chat.type.as_("chat_type"))
async def get_channel_or_supergroup_id(message: types.Message, chat_type: str, l10n: FluentLocalization):
    """
    Handler for message forwarded from channel
    or from anonymous admin writing on behalf
    of a supergroup
    :param message: Telegram message with "forward_from_chat" field not empty
    :param chat_type: parsed chat_type ("channel" or "supergroup")
    :param l10n: Fluent localization object
    """
    chat_type_str = l10n.format_value(msg_id=chat_type)
    msg = l10n.format_value(msg_id="any-chat", args={"type": chat_type_str, "id": html.code(message.forward_from_chat.id)})
    if message.sticker:
        msg += "\n" + l10n.format_value(msg_id="sticker-id", args={"id": html.code(message.sticker.file_id)})
    await message.reply(msg)


@router.message(F.forward_from)
async def get_user_id_no_privacy(message: types.Message, l10n: FluentLocalization):
    """
    Handler for message forwarded from other user who doesn't hide their ID
    :param message: Telegram message with "forward_from" field not empty
    :param l10n: Fluent localization object
    """
    account_type = "bot" if message.forward_from.is_bot else "user"
    chat_type_str = l10n.format_value(msg_id=account_type)
    msg = l10n.format_value(msg_id="any-chat", args={"type": chat_type_str, "id": html.code(message.forward_from.id)})
    if message.sticker:
        msg += "\n" + l10n.format_value(msg_id="sticker-id", args={"id": html.code(message.sticker.file_id)})
    await message.reply(msg)


@router.message(F.forward_sender_name)
async def get_user_id_with_privacy(message: types.Message, l10n: FluentLocalization):
    """
    Handler for message forwarded from other user who hides their ID
    :param message: Telegram message with "forward_sender_name" field not empty
    :param l10n: Fluent localization object
    """
    msg = l10n.format_value(msg_id="user-id-hidden")
    if message.sticker:
        msg += "\n\n" + l10n.format_value(msg_id="sticker-id", args={"id": html.code(message.sticker.file_id)})
    await message.reply(msg)


@router.message(F.sticker)
async def sticker_in_pm(message: types.Message, l10n: FluentLocalization):
    """
    /start command handler for private chats
    :param message: Telegram message with "/start" command
    :param l10n: Fluent localization object
    """
    #
    await message.reply(
        l10n.format_value(msg_id="sticker-id-extended", args={"id": html.code(message.sticker.file_id)})
    )


@router.message(F.via_bot, MagicData(F.event.via_bot.id != F.bot.id))  # noqa
async def other_inline_bot_in_pm(message: types.Message, l10n: FluentLocalization):
    """
    Message via some other inline bot in PM
    :param message: Any Telegram message
    :param l10n: Fluent localization object
    """
    bot_str = l10n.format_value(msg_id="bot")
    await message.answer(
        l10n.format_value(msg_id="any-chat", args={"type": bot_str, "id": html.code(message.via_bot.id)})
    )


@router.message(~F.via_bot)
async def other_in_pm(message: types.Message, l10n: FluentLocalization):
    """
    Any other message in PM, not via inline bot
    :param message: Any Telegram message
    :param l10n: Fluent localization object
    """
    await message.answer(l10n.format_value(msg_id="cmd-id-pm", args={"id": html.code(message.from_user.id)}))
