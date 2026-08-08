import os
import logging

from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

from handlers.start import start
from handlers.menu import show_menu
from handlers.subscription import subscribe, unsubscribe

from database import (
    initialize_database,
    add_subscriber,
    remove_subscriber,
)

from scheduler import setup_scheduler


# ============================================================
# ENVIRONMENT
# ============================================================

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


# ============================================================
# LOGGING
# ============================================================

logging.basicConfig(
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


# ============================================================
# INLINE BUTTON HANDLER
# ============================================================

async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    query = update.callback_query

    await query.answer()

    # --------------------------------------------------------
    # TODAY'S SAFETY
    # --------------------------------------------------------

    if query.data == "today":

        from services.safety_content import get_daily_safety_message

        message = get_daily_safety_message()

        await query.message.reply_text(
            message,
            parse_mode="Markdown",
        )

    # --------------------------------------------------------
    # RANDOM SAFETY
    # --------------------------------------------------------

    elif query.data == "random":

        from services.safety_content import (
            SAFETY_TOPICS,
            format_safety_message,
        )

        import random

        topic = random.choice(
            list(SAFETY_TOPICS.keys())
        )

        safety_tip = random.choice(
            SAFETY_TOPICS[topic]
        )

        message = format_safety_message(
            topic,
            safety_tip,
        )

        await query.message.reply_text(
            message,
            parse_mode="Markdown",
        )

    # --------------------------------------------------------
    # SAFETY CATEGORIES
    # --------------------------------------------------------

    elif query.data == "categories":

        message = """
📚 *LIFEGUARD 365 SAFETY CATEGORIES*

🦺 Workplace Safety
🏠 Home Safety
🚗 Road Safety
⚡ Electrical Safety
🔥 Fire Safety
💧 Water Safety
🍲 Food Safety
🧼 Health & Hygiene
💻 Cyber Safety
🌍 Environmental Safety

Choose safety today.
Protect yourself.
Protect others.
Protect life.
"""

        await query.message.reply_text(
            message,
            parse_mode="Markdown",
        )

    # --------------------------------------------------------
    # SAFETY QUIZ
    # --------------------------------------------------------

    elif query.data == "quiz":

        message = """
📝 *LIFEGUARD 365 SAFETY QUIZ*

What should you do when you discover a serious hazard?

A️⃣ Ignore it.

B️⃣ Report it immediately.

C️⃣ Walk away without telling anyone.

✅ *Correct answer: B — Report it immediately.*

A hazard that is reported can be controlled.
A hazard that is ignored can become an accident.
"""

        await query.message.reply_text(
            message,
            parse_mode="Markdown",
        )

    # --------------------------------------------------------
    # SUBSCRIBE
    # --------------------------------------------------------

    elif query.data == "subscribe":

        user = query.from_user

        add_subscriber(
            user_id=user.id,
            first_name=user.first_name or "",
            username=user.username or "",
        )

        message = """
🔔 *LIFEGUARD 365 SUBSCRIPTION ACTIVATED*

You are now subscribed to receive our automatic daily safety messages.

⏰ Daily safety awareness
🛡️ Practical safety guidance
🌍 Life awareness

One message.
One lesson.
One safer decision.

❤️ *Protect life.*
"""

        await query.message.reply_text(
            message,
            parse_mode="Markdown",
        )

    # --------------------------------------------------------
    # UNSUBSCRIBE
    # --------------------------------------------------------

    elif query.data == "unsubscribe":

        user = query.from_user

        remove_subscriber(user.id)

        message = """
🔕 *LIFEGUARD 365 SUBSCRIPTION CANCELLED*

You will no longer receive automatic daily safety messages.

You can subscribe again at any time.

🛡️ Stay safe.
"""

        await query.message.reply_text(
            message,
            parse_mode="Markdown",
        )

    # --------------------------------------------------------
    # EMERGENCY
    # --------------------------------------------------------

    elif query.data == "emergency":

        message = """
🚨 *EMERGENCY SAFETY REMINDER*

Stay calm.

Move away from immediate danger.

Alert people nearby.

Do not put yourself in unnecessary danger while attempting to help someone else.

Contact the appropriate emergency service when necessary.

🛡️ *Safety first.*
"""

        await query.message.reply_text(
            message,
            parse_mode="Markdown",
        )

    # --------------------------------------------------------
    # HELP
    # --------------------------------------------------------

    elif query.data == "help":

        message = """
ℹ️ *LIFEGUARD 365 HELP*

Use the menu buttons to access safety information.

*Commands:*

/start — Open LifeGuard 365
/menu — Show the safety menu
/today — Today's safety message
/random — Random safety message
/subscribe — Subscribe to daily messages
/unsubscribe — Cancel subscription
/help — Show help

🛡️ *Stay safe. Stay informed. Protect life.*
"""

        await query.message.reply_text(
            message,
            parse_mode="Markdown",
        )


# ============================================================
# TODAY COMMAND
# ============================================================

async def today_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    from services.safety_content import (
        get_daily_safety_message,
    )

    message = get_daily_safety_message()

    await update.message.reply_text(
        message,
        parse_mode="Markdown",
    )


# ============================================================
# RANDOM COMMAND
# ============================================================

async def random_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    from services.safety_content import (
        SAFETY_TOPICS,
        format_safety_message,
    )

    import random

    topic = random.choice(
        list(SAFETY_TOPICS.keys())
    )

    safety_tip = random.choice(
        SAFETY_TOPICS[topic]
    )

    message = format_safety_message(
        topic,
        safety_tip,
    )

    await update.message.reply_text(
        message,
        parse_mode="Markdown",
    )


# ============================================================
# HELP COMMAND
# ============================================================

async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    message = """
ℹ️ *LIFEGUARD 365 HELP*

Your Daily Safety & Life Awareness Assistant.

*Commands:*

/start — Open the bot
/menu — Show the safety menu
/today — Today's safety message
/random — Random safety message
/subscribe — Receive daily messages
/unsubscribe — Stop daily messages
/help — Show help

🛡️ Stay safe.
💡 Stay informed.
❤️ Protect life.
"""

    await update.message.reply_text(
        message,
        parse_mode="Markdown",
    )


# ============================================================
# MAIN APPLICATION
# ============================================================

def main():

    if not BOT_TOKEN:

        raise ValueError(
            "BOT_TOKEN environment variable is not set."
        )

    # Create database tables
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
        CommandHandler(
            "start",
            start,
        )
    )

    application.add_handler(
        CommandHandler(
            "menu",
            show_menu,
        )
    )

    application.add_handler(
        CommandHandler(
            "today",
            today_command,
        )
    )

    application.add_handler(
        CommandHandler(
            "random",
            random_command,
        )
    )

    application.add_handler(
        CommandHandler(
            "subscribe",
            subscribe,
        )
    )

    application.add_handler(
        CommandHandler(
            "unsubscribe",
            unsubscribe,
        )
    )

    application.add_handler(
        CommandHandler(
            "help",
            help_command,
        )
    )

    # --------------------------------------------------------
    # INLINE BUTTONS
    # --------------------------------------------------------

    application.add_handler(
        CallbackQueryHandler(
            button_handler
        )
    )

    # --------------------------------------------------------
    # DAILY SCHEDULER
    # --------------------------------------------------------

    setup_scheduler(
        application
    )

    logger.info(
        "🛡️ LifeGuard 365 is running..."
    )

    logger.info(
        "⏰ Daily safety broadcast scheduled "
        "for 07:00 Africa/Lagos."
    )

    # --------------------------------------------------------
    # START TELEGRAM BOT
    # --------------------------------------------------------

    application.run_polling()


# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    main()