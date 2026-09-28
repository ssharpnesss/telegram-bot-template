"""Dialog handlers package."""

from aiogram import Router

from app.dialogs.start import start_dialog

def get_dialogs_router() -> Router:
    router = Router()

    router.include_router(start_dialog)

    return router

__all__ = [
    "start_dialog",
]