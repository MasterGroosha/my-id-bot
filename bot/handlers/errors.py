import structlog
from aiogram import Router
from aiogram.exceptions import TelegramAPIError
from aiogram.types.error_event import ErrorEvent
from structlog.typing import FilteringBoundLogger

router = Router(name="errors-router")
logger: FilteringBoundLogger = structlog.get_logger()


@router.errors()
async def handle_errors(event: ErrorEvent):
    if isinstance(event.exception, TelegramAPIError):
        error_message = event.exception.message
        error_source = "BotAPI"
    else:
        error_message = str(event.exception)
        error_source = "Python"

    logger.error(
        "Outgoing bot message error",
        exception_type=event.exception.__class__.__name__,
        message=error_message,
        update=event.update.json(),
        error_source=error_source
    )
