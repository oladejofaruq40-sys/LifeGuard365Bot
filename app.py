import logging
import os

from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

from database import (
    add_subscriber,
    initialize_database,
    remove_subscriber,
)

from handlers.menu import show_menu
from handlers.start import start
from handlers.subscription import subscribe, unsubscribe

from scheduler import setup_scheduler

from services.safety_content import (
    get_categories,
    get_daily_safety_message,
    get_random_safety_message,
)


# ============================================================
# ENVIRONMENT
# ============================================================

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


# ============================================================
# LOGGING
# ============================================================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


# ============================================================
# TODAY BUTTON
# ============================================================

async def send_today(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    message = get_daily_safety_message()

    await update.callback_query.message.reply_text(
        message,
        parse_mode="Markdown",
    )


# ============================================================
# RANDOM BUTTON
# ============================================================

async def send_random(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    message = get_random_safety_message()

    await update.callback_query.message.reply_text(
        message,
        parse_mode="Markdown",
    )


# ============================================================
# CATEGORIES BUTTON
# ============================================================

async def send_categories(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

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

    await update.callback_query.message.reply_text(
        message,
        parse_mode="Markdown",
    )


# ============================================================
# QUIZ BUTTON
# ============================================================

async def send_quiz(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    message = (
        "📝 *LIFEGUARD 365 SAFETY QUIZ*\n\n"
        "You discover a serious electrical hazard "
        "in your workplace. What should you do?\n\n"
        "A️⃣ Ignore it.\n"
        "B️⃣ Report it immediately.\n"
        "C️⃣ Continue working around it.\n\n"
        "✅ *Correct answer: B — Report it immediately.*\n\n"
        "Remember: an identified hazard can be "
        "controlled before it becomes an accident."
    )

    await update.callback_query.message.reply_text(
        message,
        parse_mode="Markdown",
    )


# ============================================================
# SUBSCRIBE BUTTON
# ============================================================

async def button_subscribe(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    user = update.callback_query.from_user

    add_subscriber(
        user_id=user.id,
        first_name=user.first_name or "",
        username=user.username or "",
    )

    message = (
        "🔔 *SUBSCRIPTION ACTIVATED*\n\n"
        "You are now subscribed to receive "
        "LifeGuard 365 daily safety messages.\n\n"
        "🛡️ One message.\n"
        "💡 One lesson.\n"
        "❤️ One safer decision.\n\n"
        "Stay safe. Stay informed. Protect life."
    )

    await update.callback_query.message.reply_text(
        message,
        parse_mode="Markdown",
    )


# ============================================================
# UNSUBSCRIBE BUTTON
# ============================================================

async def button_unsubscribe(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    user = update.callback_query.from_user

    remove_subscriber(user.id)

    message = (
        "🔕 *SUBSCRIPTION CANCELLED*\n\n"
        "You will no longer receive automatic "
        "LifeGuard 365 daily safety messages.\n\n"
        "You can subscribe again anytime."
    )

    await update.callback_query.message.reply_text(
        message,
        parse_mode="Markdown",
    )


# ============================================================
# EMERGENCY BUTTON
# ============================================================

async def emergency_safety(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    message = (
        "🚨 *EMERGENCY SAFETY REMINDER*\n\n"
        "Stay calm.\n\n"
        "Move away from immediate danger.\n\n"
        "Alert people nearby when safe to do so.\n\n"
        "Do not put yourself in unnecessary danger "
        "while attempting to help another person.\n\n"
        "Contact the appropriate emergency service "
        "when necessary.\n\n"
        "🛡️ *Safety first.*"
    )

    await update.callback_query.message.reply_text(
        message,
        parse_mode="Markdown",
    )


# ============================================================
# HELP BUTTON
# ============================================================

async def show_help(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    message = (
        "ℹ️ *LIFEGUARD 365 HELP*\n\n"
        "Your Daily Safety & Life Awareness Assistant.\n\n"
        "*Commands:*\n\n"
        "/start — Open LifeGuard 365\n"
        "/menu — Open the safety dashboard\n"
        "/today — Today's safety message\n"
        "/random — Random safety message\n"
        "/subscribe — Receive daily messages\n"
        "/unsubscribe — Stop daily messages\n"
        "/help — Show help\n\n"
        "🛡️ Stay safe.\n"
        "💡 Stay informed.\n"
        "❤️ Protect life."
    )

    await update.callback_query.message.reply_text(
        message,
        parse_mode="Markdown",
    )


# ============================================================
# CALLBACK ROUTER
# ============================================================

async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    query = update.callback_query

    await query.answer()

    if query.data == "today":
        await send_today(update, context)

    elif query.data == "random":
        await send_random(update, context)

    elif query.data == "categories":
        await send_categories(update, context)

    elif query.data == "quiz":
        await send_quiz(update, context)

    elif query.data == "subscribe":
        await button_subscribe(update, context)

    elif query.data == "unsubscribe":
        await button_unsubscribe(update, context)

    elif query.data == "emergency":
        await emergency_safety(update, context)

    elif query.data == "help":
        await show_help(update, context)


# ============================================================
# COMMAND: TODAY
# ============================================================

async def today_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    message = get_daily_safety_message()

    await update.message.reply_text(
        message,
        parse_mode="Markdown",
    )


# ============================================================
# COMMAND: RANDOM
# ============================================================

async def random_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    message = get_random_safety_message()

    await update.message.reply_text(
        message,
        parse_mode="Markdown",
    )


# ============================================================
# COMMAND: HELP
# ============================================================

async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    message = (
        "ℹ️ *LIFEGUARD 365 HELP*\n\n"
        "Use /menu to open the safety dashboard.\n\n"
        "/start — Start the bot\n"
        "/menu — Safety dashboard\n"
        "/today — Today's safety message\n"
        "/random — Random safety message\n"
        "/subscribe — Subscribe\n"
        "/unsubscribe — Unsubscribe\n"
        "/help — Help\n\n"
        "🛡️ Stay safe. Stay informed. Protect life."
    )

    await update.message.reply_text(
        message,
        parse_mode="Markdown",
    )


# ============================================================
# MAIN
# ============================================================

def main():

    if not BOT_TOKEN:

        raise RuntimeError(
            "BOT_TOKEN environment variable is not set."
        )

    # Initialize SQLite database
    initialize_database()

    # Create Telegram application
    application = (
        Application
        .builder()
        .token(BOT_TOKEN)
        .build()
    )

    # --------------------------------------------------------
    # COMMAND HANDLERS
    # --------------------------------------------------------

    application.add_handler(
        CommandHandler("start", start)
    )

    application.add_handler(
        CommandHandler("menu", show_menu)
    )

    application.add_handler(
        CommandHandler("today", today_command)
    )

    application.add_handler(
        CommandHandler("random", random_command)
    )

    application.add_handler(
        CommandHandler("subscribe", subscribe)
    )

    application.add_handler(
        CommandHandler("unsubscribe", unsubscribe)
    )

    application.add_handler(
        CommandHandler("help", help_command)
    )

    # --------------------------------------------------------
    # INLINE BUTTON HANDLER
    # --------------------------------------------------------

    application.add_handler(
        CallbackQueryHandler(button_handler)
    )

    # --------------------------------------------------------
    # DAILY SCHEDULER
    # --------------------------------------------------------

    setup_scheduler(application)

    logger.info(
        "🛡️ LifeGuard 365 is running..."
    )

    logger.info(
        "⏰ Daily safety broadcast scheduled "
        "for 07:00 Africa/Lagos."
    )

    # --------------------------------------------------------
    # START BOT
    # --------------------------------------------------------

    application.run_polling()


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()