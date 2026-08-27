from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from services.safety_content import SAFETY_TOPICS


def category_keyboard():
    """Create the safety category selection keyboard."""

    keyboard = []

    for category in SAFETY_TOPICS.keys():
        keyboard.append(
            [
                InlineKeyboardButton(
                    category,
                    callback_data=f"category:{category}",
                )
            ]
        )

    keyboard.append(
        [
            InlineKeyboardButton(
                "🏠 Main Menu",
                callback_data="menu",
            )
        ]
    )

    return InlineKeyboardMarkup(keyboard)


async def show_category_menu(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    """Display all available safety categories."""

    query = update.callback_query

    if query:
        await query.answer()

    message = (
        "📚 *LIFEGUARD 365 SAFETY CATEGORIES*\n\n"
        "Choose a safety area below:\n\n"
        "🛡️ Learn.\n"
        "⚠️ Identify hazards.\n"
        "❤️ Protect life."
    )

    if query:
        await query.message.reply_text(
            message,
            reply_markup=category_keyboard(),
            parse_mode="Markdown",
        )
    else:
        await update.message.reply_text(
            message,
            reply_markup=category_keyboard(),
            parse_mode="Markdown",
        )


async def show_category(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    """Display a safety tip from the selected category."""

    query = update.callback_query
    await query.answer()

    category = query.data.split(":", 1)[1]

    if category not in SAFETY_TOPICS:
        await query.message.reply_text(
            "⚠️ Sorry, that safety category could not be found."
        )
        return

    import random

    safety_tip = random.choice(SAFETY_TOPICS[category])

    message = (
        f"🛡️ *LIFEGUARD 365*\n\n"
        f"📚 *{category.upper()}*\n\n"
        f"{safety_tip}\n\n"
        "━━━━━━━━━━━━━━\n\n"
        "💡 *SAFETY REMINDER*\n"
        "A few seconds of caution can prevent "
        "a lifetime of regret.\n\n"
        "Protect yourself.\n"
        "Protect others.\n"
        "Protect life."
    )

    keyboard = [
        [
            InlineKeyboardButton(
                "🔄 Another Tip",
                callback_data=f"category:{category}",
            )
        ],
        [
            InlineKeyboardButton(
                "📚 Categories",
                callback_data="categories",
            ),
            InlineKeyboardButton(
                "🏠 Main Menu",
                callback_data="menu",
            ),
        ],
    ]

    await query.message.reply_text(
        message,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown",
    )
