from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from .keyboards import build_main_menu_keyboard


async def start_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    text = (
        "🩺 Headache Log\n\n"
        "Отслеживайте приступы головной боли и мигрени.\n\n"
        "Выберите действие:"
    )

    await update.message.reply_text(
        text=text,
        reply_markup=build_main_menu_keyboard(),
    )


handler = CommandHandler("start", start_command)
