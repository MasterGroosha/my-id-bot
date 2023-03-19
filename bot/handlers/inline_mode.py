from aiogram import types, html, Router
from aiogram.enums import ChatType
from fluent.runtime import FluentLocalization

router = Router()


@router.inline_query()
async def inline_mode_handler(query: types.InlineQuery, l10n: FluentLocalization):
    result = types.InlineQueryResultArticle(
        id=".",
        title=l10n.format_value(msg_id="inline-mode-title", args={"id": query.from_user.id}),
        description=l10n.format_value(msg_id="inline-mode-description"),
        input_message_content=types.InputTextMessageContent(
            message_text=l10n.format_value(msg_id="inline-mode-text", args={"id": html.code(query.from_user.id)})
        )
    )
    # Do not forget about is_personal parameter! Otherwise, all people will see the same ID
    switch_pm_text = l10n.format_value(msg_id="inline-mode-tryme") if query.chat_type != ChatType.SENDER else None
    await query.answer(
        results=[result], cache_time=3600, is_personal=True,
        switch_pm_parameter="1", switch_pm_text=switch_pm_text
    )
