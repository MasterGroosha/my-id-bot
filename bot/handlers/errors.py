from aiogram import Router
from aiogram.types.error_event import ErrorEvent

router = Router()


@router.errors()
async def errors_handler(event: ErrorEvent):
    # Not very good, but for now it's okay
    print(f"Error: {str(event.exception)}. Update: {event.update.dict()}")
