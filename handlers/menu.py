from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
)
from telegram.ext import ContextTypes


def build_main_menu():
    """
    Build the main LifeGuard 365 interactive menu.
    """

    keyboard = [
        [
            InlineKeyboardButton(
                "🛡️ Today's Safety",
                callback_data="today",
            ),
            InlineKeyboardButton(
                "🎲 Random Safety",
                callback_data="random",
            ),
        ],
        [
            InlineKeyboardButton(
                "📚 Safety Categories",
                callback_data="categories",
            ),
            InlineKeyboardButton(
                "📝 Safety Quiz",
                callback_data="quiz",
            ),
        ],
        [
            InlineKeyboardButton(
                "🔔 Subscribe",
                callback_data="subscribe",
            ),
            InlineKeyboardButton(
                "🔕 Unsubscribe",
                callback_data="unsubscribe",
            ),
        ],
        [
            InlineKeyboardButton(
                "🚨 Emergency Safety",
                callback_data="emergency",
            ),
        ],
        [
            InlineKeyboardButton(
                "ℹ️ Help",
                callback_data="help",
            ),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


async def show_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    """
    Display the LifeGuard 365 main menu.
    """

    message = (
        "🛡️ *LIFEGUARD 365*\n\n"
        "Welcome to your Daily Safety & Life Awareness "
        "Dashboard.\n\n"
        "Choose an option below:\n\n"
        "🛡️ Get today's safety message\n"
        "🎲 Discover a random safety tip\n"
        "📚 Explore safety categories\n"
        "📝 Test your safety knowledge\n"
        "🔔 Subscribe to daily alerts\n"
        "🚨 Get emergency safety guidance\n"
        "ℹ️ Learn how the bot works\n\n"
        "*One message. One lesson. One safer decision.*"
    )

    await update.message.reply_text(
        message,
        reply_markup=build_main_menu(),
        parse_mode="Markdown",
    )