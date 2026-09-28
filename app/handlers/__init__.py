from aiogram import Router

def get_handlers() -> Router:
    from .user import get_user_handlers
    router = Router()

    router.include_router(get_user_handlers())
    
    return router
