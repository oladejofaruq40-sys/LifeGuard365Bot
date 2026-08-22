from telegram import Update
from telegram.ext import ContextTypes

from services.safety_content import (
    get_categories,
    get_daily_safety_message,
    get_random_safety_message,
)


async def send_today(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    """Send today's safety message."""

    message = get_daily_safety_message()

    if update.callback_query:
        await update.callback_query.message.reply_text(
            message,
            parse_mode="Markdown",
        )
    else:
        await update.message.reply_text(
            message,
            parse_mode="Markdown",
        )


async def send_random(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    """Send a random safety message."""

    message = get_random_safety_message()

    if update.callback_query:
        await update.callback_query.message.reply_text(
            message,
            parse_mode="Markdown",
        )
    else:
        await update.message.reply_text(
            message,
            parse_mode="Markdown",
        )


async def send_categories(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    """Display available safety categories."""

    categories = get_categories()

    category_text = "\n".join(
        f"• {category}"
        for category in categories
    )

    message = (
        "📚 *LIFEGUARD 365 SAFETY CATEGORIES*\n\n"
        f"{category_text}\n\n"
        "Our mission is simple:\n"
        "🛡️ Create awareness.\n"
        "⚠️ Identify hazards.\n"
        "❤️ Protect life."
    )

    if update.callback_query:
        await update.callback_query.message.reply_text(
            message,
            parse_mode="Markdown",
        )
    else:
        await update.message.reply_text(
            message,
            parse_mode="Markdown",
        )
