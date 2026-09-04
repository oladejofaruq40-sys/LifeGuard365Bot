from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from database.database import get_user_progress


async def show_progress(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    """Display the user's LifeGuard 365 safety progress."""

    user = update.effective_user

    if not user:
        return

    progress = get_user_progress(user.id)

    quiz_completed = progress.get("quiz_completed", 0)
    quiz_correct = progress.get("quiz_correct", 0)
    tips_viewed = progress.get("tips_viewed", 0)

    if quiz_completed > 0:
        total_questions = quiz_completed * 5
        accuracy = int((quiz_correct / total_questions) * 100)
    else:
        accuracy = 0

    if accuracy >= 90:
        level = "🏆 Safety Champion"
    elif accuracy >= 80:
        level = "🥇 Safety Defender"
    elif accuracy >= 60:
        level = "🥈 Safety Learner"
    else:
        level = "🛡️ Safety Beginner"

    message = (
        "🏆 *YOUR LIFEGUARD 365 PROGRESS*\n\n"
        f"🔥 *Current Streak:* {progress['current_streak']} days\n"
        f"🏅 *Longest Streak:* {progress['longest_streak']} days\n\n"
        f"📚 *Safety Tips Viewed:* {tips_viewed}\n"
        f"🧠 *Quizzes Completed:* {quiz_completed}\n"
        f"✅ *Correct Answers:* {quiz_correct}\n"
        f"🎯 *Quiz Accuracy:* {accuracy}%\n\n"
        f"*Safety Level:* {level}\n\n"
        "━━━━━━━━━━━━━━\n\n"
        "🛡️ Keep learning.\n"
        "⚠️ Stay alert.\n"
        "❤️ Protect life."
    )

    keyboard = [
        [
            InlineKeyboardButton(
                "🧠 Take Safety Quiz",
                callback_data="quiz",
            )
        ],
        [
            InlineKeyboardButton(
                "📚 Safety Categories",
                callback_data="categories",
            ),
            InlineKeyboardButton(
                "🏠 Main Menu",
                callback_data="menu",
            ),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.callback_query:
        await update.callback_query.message.reply_text(
            message,
            reply_markup=reply_markup,
            parse_mode="Markdown",
        )
    else:
        await update.message.reply_text(
            message,
            reply_markup=reply_markup,
            parse_mode="Markdown",
        )
