from telegram import Update, 
InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
def main_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(" Daily Safety", 
callback_data="today"),
            InlineKeyboardButton(" Random Tip", 
callback_data="random"),
        ],
        [
            InlineKeyboardButton(" Safety Categories", 
callback_data="categories"),
            InlineKeyboardButton(" Safety Quiz", 
callback_data="quiz"),
        ],
        [
            InlineKeyboardButton(" Subscribe", 
callback_data="subscribe"),
            InlineKeyboardButton(" Unsubscribe", 
callback_data="unsubscribe"),
        ],
        [
            InlineKeyboardButton(" Emergency Tips", 
callback_data="emergency"),
            InlineKeyboardButton(" Help", 
callback_data="help"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
async def show_menu(update: Update, context: 
ContextTypes.DEFAULT_TYPE):
    message = """
 *LIFEGUARD 365*
*Your Daily Safety & Life Awareness Assistant*
Choose what you want to learn today:
 Workplace & Industrial Safety
 Home & Family Safety
 Road & Transportation Safety
 Electrical Safety
 Fire Prevention
 Water Safety
 Food Safety
 Health & Wellbeing
 Cyber Safety
 Environmental Safety
 Emergency Preparedness
*One good safety decision can change a life.*
Stay alert. Stay safe. Protect life. 
"""
    if update.message:
        await update.message.reply_text(
            message,
            parse_mode="Markdown",
            reply_markup=main_menu_keyboard()
        )