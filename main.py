import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello, welcome to My Bot by Pushpak Jaiswal.")

async def helps(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        """Hi There! I'm a Telegram bot created by Pushpak Jaiswal. Please follow these commands:
        /start - To start the conversation.
        /content - Information about the bot.
        /contact - Information to contact Pushpak Jaiswal.
        /help - To get this help menu.
        
        I hope this helps! :) 
        """
    )

async def content(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        """This bot is created by Pushpak Jaiswal. It is built using the following technologies:
        - Python
        - python-telegram-bot library
        - dotenv for environment variable management
        
        The bot provides various functionalities and helps you to interact with it using simple commands.
        """
    )

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("You can contact Pushpak Jaiswal at pushpakmjaiswal@gmail.com.")

# Create the Application
app = ApplicationBuilder().token(TOKEN).build()

# Add handlers to the dispatcher
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', helps))
app.add_handler(CommandHandler('content', content))
app.add_handler(CommandHandler('contact', contact))

# Start the bot
app.run_polling()