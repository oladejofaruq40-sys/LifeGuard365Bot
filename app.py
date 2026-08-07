import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")


# ==========================
# Commands
# ==========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to *LifeGuard 365!*\n\n"
        "Your trusted Daily Safety & Life Awareness Bot.\n\n"
        "Available commands:\n"
        "/today - Today's safety tip\n"
        "/random - Random safety tip\n"
        "/subscribe - Receive daily safety messages\n"
        "/help - Show help",
        parse_mode="Markdown",
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 LifeGuard365 Help\n\n"
        "/start\n"
        "/today\n"
        "/random\n"
        "/subscribe\n"
        "/unsubscribe\n"
        "/help"
    )


async def today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🦺 Daily Safety Tip\n\n"
        "Always think before you act.\n"
        "One safe decision can prevent a lifetime of regret."
    )


# ==========================
# Main
# ==========================

def main():

    if BOT_TOKEN is None:
        raise ValueError("BOT_TOKEN not found!")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("today", today))

    print("✅ LifeGuard365 Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
