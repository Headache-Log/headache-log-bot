from telegram import Update
from telegram.ext import CallbackQueryHandler, ContextTypes

from .actions import MainMenuAction


async def handle_menu_action(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    query = update.callback_query
    await query.answer()

    action = query.data

    if action == MainMenuAction.NEW:
        await query.edit_message_text("New entry (not implemented yet)")
    elif action == MainMenuAction.HISTORY:
        await query.edit_message_text("Last 10 entries (not implemented yet)")
    elif action == MainMenuAction.EXPORT:
        await query.edit_message_text("Export CSV (not implemented yet)")
    elif action == MainMenuAction.SETTINGS:
        await query.edit_message_text("Settings (not implemented yet)")
    else:
        await query.edit_message_text("Unknown action")


handler = CallbackQueryHandler(
    handle_menu_action,
    pattern="^menu:",
)
