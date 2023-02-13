import logging
import settings
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    filename='bot.log', 
    level=logging.INFO
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Processing the start command"""
    await update.message.reply_text('Привет, пользователь! \nТы вызвал команду /start.')

async def talk_to_me(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Repeating user messages"""
    user_text = update.message.text 
    print(user_text)
    await update.message.reply_text(user_text)

def main() -> None:
    """Start the bot"""
    bot = Application.builder().token(settings.API_KEY).build()

    # Different commands
    bot.add_handler(CommandHandler('start', start))
    bot.add_handler(MessageHandler(filters.TEXT, talk_to_me))

    # Logs
    logging.info("Бот стартовал.")

    # Run the bot
    bot.run_polling()

if __name__ == "__main__":
    main()