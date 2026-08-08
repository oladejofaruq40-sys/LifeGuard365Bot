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
from scheduler import setup_scheduler
from database.database import 
initialize_database
# Load environment variables
load_dotenv()
# Logging
logging.basicConfig(
    level=logging.INFO
)
BOT_TOKEN = os.getenv("BOT_TOKEN")
async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()
    async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()
    if query.data == "today":
        message = """
 TODAY'S SAFETY TIP
Think before you act.
A few seconds of caution can prevent a serious accident.
 Stay alert.
 Identify hazards.
 Take action before someone gets hurt.
"""
        await query.message.reply_text(message)
    elif query.data == "random":
        message = """
 RANDOM SAFETY TIP
Never ignore a small hazard.
Small hazards can become serious incidents when left unattended.
 See it.
 Report it.
 Correct it.
"""
        await query.message.reply_text(message)
    elif query.data == "categories":
        message = """
 SAFETY CATEGORIES
 Workplace Safety
 Home Safety
 Road Safety
 Electrical Safety
 Fire Safety
 Water Safety
 Food Safety
 Health & Wellbeing
 Cyber Safety
 Environmental Safety
"""
        await query.message.reply_text(message)
    elif query.data == "quiz":
        message = """
 SAFETY QUIZ
What should you do when you discover a serious hazard?
A⃣ Ignore it
B⃣ Report it immediately
C⃣ Walk away without telling anyone
 Correct answer: B — Report it immediately.
"""
        await query.message.reply_text(message)
    elif query.data == "subscribe":
        user = query.from_user
        from database.database import add_subscriber
        add_subscriber(
            user_id=user.id,
            first_name=user.first_name or "",
            username=user.username or "",
        )
        message = """
 SUBSCRIPTION ACTIVATED!
You are now registered to receive the daily LifeGuard 365 safety message.
 Stay safe.
 Stay informed.
 Protect life.
"""
        await query.message.reply_text(message)
    elif query.data == "unsubscribe":
        user = query.from_user
        from database.database import remove_subscriber
        remove_subscriber(user.id)
        message = """
 SUBSCRIPTION CANCELLED
You will no longer receive automatic daily LifeGuard 365 messages.
You can subscribe again anytime.
"""
        await query.message.reply_text(message)
    elif query.data == "emergency":
        message = """
 EMERGENCY SAFETY REMINDER
Stay calm.
Move away from immediate danger.
Alert people nearby.
Contact the appropriate emergency service when necessary.
"""
        await query.message.reply_text(message)
    elif query.data == "help":
        message = """
 LIFEGUARD 365 HELP
Use the buttons on the main menu to access safety information.
Commands:
/start — Open LifeGuard 365
/menu — Show the menu
/today — Today's safety tip
/subscribe — Subscribe
/unsubscribe — Unsubscribe
/help — Help
"""
        await query.message.reply_text(message)