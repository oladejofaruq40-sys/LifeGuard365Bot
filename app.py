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
from handlers.subscription import
subscriber, unsubscriber
load_dotenv()
logging.basicConfig(
    format="%(asctime)s - %(name)s - %
(levelname)s - %(message)s",
    level=logging.INFO,
)
BOT_TOKEN = os.getenv("BOT_TOKEN")
async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()
    if query.data == "today":
        await query.message.reply_text(
            " *Today's Safety Tip*\n\n"
            "Think before you act. "
            "A few seconds of caution can prevent a 
serious accident.\n\n"
            " Stay alert. Stay safe.",
            parse_mode="Markdown",
        )
    elif query.data == "random":
        await query.message.reply_text(
            " *Random Safety Tip*\n\n"
            "Never ignore a small hazard. "
            "Small hazards can become serious incidents 
when left unattended.",
            parse_mode="Markdown",
        )
    elif query.data == "categories":
        await query.message.reply_text(
            " *Safety Categories*\n\n"
            " Workplace Safety\n"
            " Home Safety\n"
            " Road Safety\n"
            " Electrical Safety\n"
            " Fire Safety\n"
            " Water Safety\n"
            " Food Safety\n"
            " Health & Wellbeing\n"
            " Cyber Safety\n"
            " Environmental Safety",
            parse_mode="Markdown",
        )
    elif query.data == "quiz":
        await query.message.reply_text(
            " *Safety Quiz*\n\n"
            "Question:\n"
            "What should you do when you discover a 
serious hazard?\n\n"
            "A⃣
            "B⃣
 Ignore it\n"
 Report it immediately\n"
            "C⃣ Walk away without telling anyone\n\n"
            "Correct answer: *B — Report it 
immediately.*",
            parse_mode="Markdown",
        )
    elif query.data == "subscribe":
    user = query.from_user
    from database.database import add_subscriber
    add_subscriber(
        user_id=user.id,
        first_name=user.first_name or "",
        username=user.username or "",
    )
    await query.message.reply_text(
        " *Subscription Activated!*\n\n"
        "You are now registered to receive the daily "
        "LifeGuard 365 safety message.\n\n"
        " Stay safe. Stay informed. Protect life.",
        parse_mode="Markdown",
    )
   elif query.data == "unsubscribe":
    user = query.from_user
    from database.database import remove_subscriber
    remove_subscriber(user.id)
    await query.message.reply_text(
        " *Subscription Cancelled.*\n\n"
        "You will no longer receive automatic daily "
        "LifeGuard 365 messages.\n\n"
        "You can subscribe again anytime.",
        parse_mode="Markdown",
    )
    elif query.data == "emergency":
        await query.message.reply_text(
            " *Emergency Safety Reminder*\n\n"
            "Stay calm, move away from immediate 
danger, "
            "alert people nearby, and contact the 
appropriate emergency service "
            "when necessary.",
            parse_mode="Markdown",
        )
    elif query.data == "help":
        await query.message.reply_text(
            " *LifeGuard 365 Help*\n\n"
            "Use the buttons on the main menu to access 
safety information.\n\n"
            "More features are coming soon.",
            parse_mode="Markdown",
        )
async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        " *LifeGuard 365 Help*\n\n"
        "/start — Open LifeGuard 365\n"
        "/menu — Show the safety menu\n"
        "/help — Show this help message",
        parse_mode="Markdown",
    )
def main():
    initialize_database()
    if not BOT_TOKEN:
        raise ValueError(
            "BOT_TOKEN is missing. "
            "Add it as an environment variable on 
Railway."
        )
    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )
    setup_scheduler(application)
    application.add_handler(
        CommandHandler("start", start)
    )
    application.add_handler(
        CommandHandler("menu", show_menu)
    )
    application.add_handler(
        CommandHandler("help", help_command)
    )
    application.add_handler(
        CommandHandler("subscribe",
    subscribe)
    )
    application.add_handler(
        CommandHandler("unsubscribe",
    unsubscribe)
    )
    application.add_handler(
        CallbackQueryHandler(button_handler)
    )
    print(" LifeGuard 365 is running...")
    application.run_polling()
if __name__ == "__main__":
    main()