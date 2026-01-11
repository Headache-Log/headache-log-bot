from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from .actions import MainMenuAction


def build_main_menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("➕ New entry", callback_data=MainMenuAction.NEW)],
        [InlineKeyboardButton("📄 Show history", callback_data=MainMenuAction.HISTORY)],
        [InlineKeyboardButton("📤 Export CSV", callback_data=MainMenuAction.EXPORT)],
        [InlineKeyboardButton("⚙️ Settings", callback_data=MainMenuAction.SETTINGS)],
    ]

    return InlineKeyboardMarkup(keyboard)
