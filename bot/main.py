from telegram.ext import Application

from bot.config import BOT_TOKEN
from bot.handlers import start_handler, menu_handler


def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(start_handler)
    application.add_handler(menu_handler)

    application.run_polling()


if __name__ == "__main__":
    main()
