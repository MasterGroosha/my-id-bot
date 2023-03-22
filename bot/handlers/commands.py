from aiogram import Router, html, F
from aiogram.enums import ChatType
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from fluent.runtime import FluentLocalization

router = Router()
router.message.filter(~F.forward_from & ~F.forward_from_chat)


@router.message(F.chat.type == ChatType.PRIVATE, CommandStart())
async def cmd_start(message: Message, l10n: FluentLocalization):
    """
    /start command handler for private chats
    :param message: Telegram message with "/start" command
    :param l10n: Fluent localization object
    """
    builder = InlineKeyboardBuilder()
    builder.button(text=l10n.format_value("cmd-start-inline-try-here"), switch_inline_query_current_chat="")
    builder.button(text=l10n.format_value("cmd-start-inline-try-other"), switch_inline_query="")
    await message.answer(
        l10n.format_value("cmd-start", args={"id": html.code(message.chat.id)}),
        reply_markup=builder.adjust(1).as_markup()
    )


@router.message(F.chat.type == ChatType.PRIVATE, Command("id"))
async def cmd_id_pm(message: Message, l10n: FluentLocalization):
    """
    /id command handler for private messages
    :param message: Telegram message with "/id" command
    :param l10n: Fluent localization object
    """
    await message.answer(
        l10n.format_value("cmd-id-pm", args={"id": html.code(message.from_user.id)})
    )


@router.message(
    F.chat.type.in_({ChatType.GROUP, ChatType.SUPERGROUP}),
    Command("id")
)
@router.message(
    F.chat.type.in_({ChatType.GROUP, ChatType.SUPERGROUP}),
    CommandStart(deep_link=True, magic=F.args == "id")
)
async def cmd_id_groups(message: Message, l10n: FluentLocalization):
    """
    /id command handler for (super)groups
    :param message: Telegram message with "/id" command
    :param l10n: Fluent localization object
    """
    chat_type_str = l10n.format_value(message.chat.type)
    msg = [l10n.format_value("any-chat", args={"type": chat_type_str, "id": html.code(message.chat.id)})]

    if message.is_topic_message:
        msg.append(
            l10n.format_value(
                "cmd-id-group-topic-id",
                args={"type": message.chat.type, "id": html.code(message.message_thread_id)}
            )
        )

    if message.sender_chat is None:
        msg.append(l10n.format_value("cmd-id-pm", args={"id": html.code(message.from_user.id)}))
    else:
        msg.append(l10n.format_value("cmd-id-group-as-channel", args={"id": html.code(message.sender_chat.id)}))

    await message.reply("\n".join(msg))


@router.message(Command("help"))
async def cmd_help(message: Message, l10n: FluentLocalization):
    """
    /help command handler for all chats
    :param message: Telegram message with "/help" command
    :param l10n: Fluent localization object
    """
    await message.answer(l10n.format_value("cmd-help"), disable_web_page_preview=True)
