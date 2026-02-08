"""
Cash Bot - Telegram bot for personal finance management.

This is a basic echo bot implementation that responds with the same message
it receives from the user.
"""

import logging
import os
from typing import Final

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Load environment variables from .env file
load_dotenv()

# Bot token from environment variable
TOKEN: Final = os.getenv("TELEGRAM_BOT_TOKEN")

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle the /start command.
    
    Sends a welcome message to the user when they first interact with the bot.
    
    Args:
        update: Telegram update object containing message data
        context: Callback context for the handler
    """
    user = update.effective_user
    welcome_message = (
        f"Hello, {user.first_name}! 👋\n\n"
        "I'm Cash Bot, your personal finance assistant.\n"
        "For now, I'll echo back any message you send me.\n\n"
        "Try sending me a message!"
    )
    await update.message.reply_text(welcome_message)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle the /help command.
    
    Provides information about available bot commands and features.
    
    Args:
        update: Telegram update object containing message data
        context: Callback context for the handler
    """
    help_text = (
        "🤖 *Cash Bot Help*\n\n"
        "Available commands:\n"
        "/start - Start the bot and see welcome message\n"
        "/help - Show this help message\n\n"
        "📝 For now, just send me any text message and I'll echo it back to you!"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")


async def echo_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Echo back the received message to the user.
    
    This handler responds with the same text that was sent by the user,
    demonstrating basic message handling functionality.
    
    Args:
        update: Telegram update object containing message data
        context: Callback context for the handler
    """
    user_message =   update.message.text
    logger.info("User" + str(update.effective_user.id) + str(user_message))
    
    # Echo the message back to the user
    await update.message.reply_text(user_message)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error(f"Update {update} caused error: {context.error}")
    
    # Notify user about the error if possible
    if update and update.effective_message:
        await update.effective_message.reply_text(
            "Sorry, something went wrong. Please try again later."
        )


def main() -> None:
    """
    Initialize and run the Telegram bot.
    
    Sets up handlers for commands and messages, then starts polling for updates.
    Validates that the bot token is properly configured before starting.
    
    Raises:
        ValueError: If TELEGRAM_BOT_TOKEN is not set in environment variables
    """
    if not TOKEN:
        raise ValueError(
            "TELEGRAM_BOT_TOKEN not found. "
            "Please set it in your .env file or environment variables."
        )
    
    logger.info("Starting Cash Bot...")
    
    # Create the Application instance
    application = Application.builder().token(TOKEN).build()
    
    # Register command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    
    # Register message handler for text messages (echo functionality)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_message))
    
    # Register error handler
    application.add_error_handler(error_handler)
    
    logger.info("Bot is running. Press Ctrl+C to stop.")
    
    # Start the bot with polling
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
