from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


def main_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🛡️ Today's Safety", callback_data="today"),
            InlineKeyboardButton("🎲 Random Safety", callback_data="random"),
        ],
        [
            InlineKeyboardButton("🔔 Subscribe", callback_data="subscribe"),
            InlineKeyboardButton("🔕 Unsubscribe", callback_data="unsubscribe"),
        ],
        [
            InlineKeyboardButton("📚 Safety Categories", callback_data="categories"),
            InlineKeyboardButton("ℹ️ Help", callback_data="help"),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


async def show_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛡️ *LifeGuard 365 Menu*\n\n"
        "Choose an option below:",
        reply_markup=main_menu_keyboard(),
        parse_mode="Markdown",
    )