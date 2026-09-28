"""User handlers package."""

from aiogram import Router

def get_user_handlers() -> Router:
    from app.dialogs import get_dialogs_router
    from . import start
    
    router = Router()

    router.include_router(get_dialogs_router())
    router.include_router(start.router)

    return router