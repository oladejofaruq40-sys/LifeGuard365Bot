from telegram import InlineKeyboardButton, InlineKeyboardMarkup


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