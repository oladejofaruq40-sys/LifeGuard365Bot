from telegram import Update
from telegram.ext import ContextTypes

from database import (
    add_subscriber,
    remove_subscriber,
)


async def subscribe(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    """
    Subscribe a Telegram user to daily LifeGuard 365 messages.
    """

    user = update.effective_user

    add_subscriber(
        user_id=user.id,
        first_name=user.first_name or "",
        username=user.username or "",
    )

    message = (
        "🔔 *LIFEGUARD 365 SUBSCRIPTION ACTIVATED*\n\n"
        "You are now subscribed to receive our "
        "automatic daily Safety & Life Awareness message.\n\n"
        "🛡️ Daily safety awareness\n"
        "💡 Practical safety guidance\n"
        "🌍 Life awareness\n\n"
        "One message.\n"
        "One lesson.\n"
        "One safer decision.\n\n"
        "❤️ *Protect life.*"
    )

    await update.message.reply_text(
        message,
        parse_mode="Markdown",
    )


async def unsubscribe(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    """
    Remove a Telegram user from daily LifeGuard 365 messages.
    """

    user = update.effective_user

    remove_subscriber(user.id)

    message = (
        "🔕 *LIFEGUARD 365 SUBSCRIPTION CANCELLED*\n\n"
        "You will no longer receive automatic "
        "daily safety messages.\n\n"
        "You can subscribe again at any time using "
        "/subscribe.\n\n"
        "🛡️ *Stay safe.*"
    )

    await update.message.reply_text(
        message,
        parse_mode="Markdown",
    )