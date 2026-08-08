from telegram import Update
from telegram.ext import ContextTypes

from services.safety_content import get_daily_safety_message


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    """
    Handles the /start command.
    """

    user = update.effective_user

    first_name = user.first_name or "Friend"

    message = (
        f"👋 *Welcome, {first_name}!*\n\n"
        "🛡️ *LIFEGUARD 365*\n"
        "Your Daily Safety & Life Awareness Assistant.\n\n"
        "Every day, LifeGuard 365 delivers practical "
        "safety awareness designed to help you:\n\n"
        "🧠 Think before you act.\n"
        "⚠️ Recognize hazards.\n"
        "🛡️ Prevent accidents.\n"
        "❤️ Protect life.\n\n"
        "Use /menu to explore the LifeGuard 365 "
        "safety features.\n\n"
        "📢 You can also use /subscribe to receive "
        "our automatic daily safety message.\n\n"
        "Stay safe.\n"
        "Stay informed.\n"
        "Protect life.\n\n"
        "— *LifeGuard 365*"
    )

    await update.message.reply_text(
        message,
        parse_mode="Markdown",
    )