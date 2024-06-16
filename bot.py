import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from handlers.admin_commands import ban, unban, kick, mute, unmute
from handlers.general_commands import start, couple, show_help

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

def main() -> None:
    # Replace 'YOUR_TOKEN' with your bot's token
    updater = Updater("6939532989:AAE5TDOAmzQ8MEfLlbEIUUVoVsDOOb0ukhc", request_kwargs={'read_timeout': 20, 'connect_timeout': 20})

    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("ban", ban))
    dispatcher.add_handler(CommandHandler("unban", unban, pass_args=True))
    dispatcher.add_handler(CommandHandler("kick", kick))
    dispatcher.add_handler(CommandHandler("mute", mute))
    dispatcher.add_handler(CommandHandler("unmute", unmute))
    dispatcher.add_handler(CallbackQueryHandler(button_click))

    # Start the Bot
    updater.start_polling()
    updater.idle()

def button_click(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if query.data == 'help_commands':
        show_help(query, context)
    else:
        query.answer()
        query.edit_message_text(text=f"Selected option: {query.data}")

if __name__ == '__main__':
    main()
