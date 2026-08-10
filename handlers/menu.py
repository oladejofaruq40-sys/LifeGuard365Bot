from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


async def show_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    keyboard = [
        [
            InlineKeyboardButton(
                "🛡️ Today's Safety Tip",
                callback_data="today"
            ),
            InlineKeyboardButton(
                "🎲 Random Safety Tip",
                callback_data="random"
            ),
        ],
        [
            InlineKeyboardButton(
                "📚 Safety Categories",
                callback_data="categories"
            ),
            InlineKeyboardButton(
                "🧠 Safety Quiz",
                callback_data="quiz"
            ),
        ],
        [
            InlineKeyboardButton(
                "🔔 Subscribe",
                callback_data="subscribe"
            ),
            InlineKeyboardButton(
                "🔕 Unsubscribe",
                callback_data="unsubscribe"
            ),
        ],
        [
            InlineKeyboardButton(
                "🚨 Emergency Reminder",
                callback_data="emergency"
            ),
            InlineKeyboardButton(
                "❓ Help",
                callback_data="help"
            ),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🛡️ *LIFEGUARD 365*\n\n"
        "Your personal daily safety and life-awareness "
        "companion.\n\n"
        "Choose an option below:",
        reply_markup=reply_markup,
        parse_mode="Markdown",
    )