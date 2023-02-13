import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(
    filename='bot.log', 
    level=logging.INFO
    )

def start(update, context) -> None:
    """Processing the start command"""
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! \nТы вызвал команду /start.')

def talk_to_me(update, context) -> None:
    """Repeating user messages"""
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def main() -> None:
    """Start the bot"""
    bot = Updater(settings.API_KEY, use_context=True)

    # Different commands
    dp = bot.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    # Logs
    logging.info("Бот стартовал.")

    # Run the bot
    bot.start_polling()
    bot.idle()

if __name__ == "__main__":
    main()