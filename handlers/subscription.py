from telegram import Update
from telegram.ext import ContextTypes

from database import (
    add_subscriber,
    remove_subscriber,
)


async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    add_subscriber(
        user_id=user.id,
        first_name=user.first_name or "",
        username=user.username or "",
    )

    await update.message.reply_text(
        "*LifeGuard 365 Subscription Activated!*\n\n"
        "You are now subscribed to receive our daily "
        "Safety & Life Awareness message.\n\n"
        "One message.\n"
        "One lesson.\n"
        "One safer decision.\n\n"
        "Stay safe. Stay informed. Protect life.",
        parse_mode="Markdown",
    )


async def unsubscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    remove_subscriber(user.id)

    await update.message.reply_text(
        "*LifeGuard 365 Subscription Cancelled.*\n\n"
        "You will no longer receive the daily automatic "
        "safety messages.\n\n"
        "You can subscribe again anytime with /subscribe.",
        parse_mode="Markdown",
    )