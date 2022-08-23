from aiogram import types, html, Router

router = Router()


@router.inline_query()
async def inline_mode_handler(query: types.InlineQuery):
    result = types.InlineQueryResultArticle(
        id=".",
        title=f"Your ID is {query.from_user.id}",
        description="Tap to send your ID to current chat",
        input_message_content=types.InputTextMessageContent(
            message_text=f"My Telegram ID is {html.code(query.from_user.id)}"
        )
    )
    # Do not forget about is_personal parameter! Otherwise, all people will see the same ID
    await query.answer(
        results=[result], cache_time=3600, is_personal=True,
        switch_pm_parameter="1", switch_pm_text="Or try me in PM >>>"
    )
