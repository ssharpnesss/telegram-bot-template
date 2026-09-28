from aiogram.types import Message
from aiogram.filters.command import CommandStart
from aiogram import Router

from aiogram_dialog import DialogManager, ShowMode, StartMode

from app.dialogs.states import StartSG

router = Router()


@router.message(CommandStart())
async def cmd_start_handler(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(
        state=StartSG.main,
        mode=StartMode.RESET_STACK,
        show_mode=ShowMode.DELETE_AND_SEND
    )