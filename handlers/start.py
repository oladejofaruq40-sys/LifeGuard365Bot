from telegram import Update
from telegram.ext import ContextTypes

from database.database import initialize_database


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    initialize_database()

    user = update.effective_user

    await update.message.reply_text(
        f"🛡️ *Welcome to LifeGuard 365, {user.first_name or 'Friend'}!*\n\n"
        "Your daily companion for Safety, Awareness and Life Protection.\n\n"
        "Every day, we deliver:\n"
        "🔹 One safety message\n"
        "🔹 One practical lesson\n"
        "🔹 One safer decision\n\n"
        "Use the menu below to explore LifeGuard 365.",
        parse_mode="Markdown",
    )