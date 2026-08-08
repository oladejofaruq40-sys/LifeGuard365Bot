from telegram import Update
from telegram.ext import ContextTypes
from handlers.menu import main_menu_keyboard
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = """
 *WELCOME TO LIFEGUARD 365*
Your Daily Safety & Life Awareness Assistant.
Every day, we share practical safety knowledge designed to help you:
 Stay safer at work
 Protect your home and family
 Make safer decisions on the road
 Prevent electrical accidents
 Prevent fires
 Stay safe around water
 Protect your wellbeing
 Stay safer online
 Protect your environment
One message can change a decision.
One decision can save a life.
 *Protect yourself.*
 *Protect others.*
 *Protect life.*
Choose an option below:
"""
    await update.message.reply_text(
        welcome_message,
        parse_mode="Markdown",
        reply_markup=main_menu_keyboard(),
    )