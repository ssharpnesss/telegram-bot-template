from typing import Any

from aiogram_dialog import Dialog, DialogManager, Window, ShowMode
from aiogram_dialog.widgets.text import Const, Format

from app.dialogs.states import StartSG

async def main_getter(dialog_manager: DialogManager, **_: Any) -> dict[str, Any]:
    name = dialog_manager.event.from_user.first_name

    return {
        "name": name
    }


start_window = Window(
    Format("{name} Привет! Это aiogram_dialogs."),
    state=StartSG.main,
    getter=main_getter
)

start_dialog = Dialog(
    start_window
)