from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


QUIZ_QUESTIONS = [
    {
        "question": "What should you do when you discover a serious electrical hazard?",
        "options": [
            "Ignore it",
            "Report it immediately",
            "Continue working around it",
            "Touch it to check the problem",
        ],
        "answer": 1,
    },
    {
        "question": "What is the safest action before electrical maintenance?",
        "options": [
            "Work quickly",
            "Switch off and isolate the power",
            "Wear ordinary clothing",
            "Pour water on the equipment",
        ],
        "answer": 1,
    },
    {
        "question": "What should you do if a fire starts?",
        "options": [
            "Hide the fire",
            "Raise the alarm and move to safety",
            "Continue working",
            "Open all electrical panels",
        ],
        "answer": 1,
    },
    {
        "question": "What should you do before driving a vehicle?",
        "options": [
            "Use your phone",
            "Wear your seatbelt",
            "Increase your speed",
            "Ignore road conditions",
        ],
        "answer": 1,
    },
    {
        "question": "Which practice helps prevent slips and falls at home?",
        "options": [
            "Leave water on the floor",
            "Clean water spills immediately",
            "Walk faster",
            "Ignore wet areas",
        ],
        "answer": 1,
    },
]


async def start_quiz(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    """Start a new LifeGuard 365 safety quiz."""

    context.user_data["quiz_score"] = 0
    context.user_data["quiz_question"] = 0

    await send_question(update, context)


async def send_question(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    """Send the current quiz question."""

    question_index = context.user_data.get("quiz_question", 0)

    if question_index >= len(QUIZ_QUESTIONS):
        await finish_quiz(update, context)
        return

    question = QUIZ_QUESTIONS[question_index]

    keyboard = []

    for index, option in enumerate(question["options"]):
        keyboard.append(
            [
                InlineKeyboardButton(
                    f"{chr(65 + index)}. {option}",
                    callback_data=f"quiz_answer:{index}",
                )
            ]
        )

    keyboard.append(
        [
            InlineKeyboardButton(
                "❌ Exit Quiz",
                callback_data="quiz_exit",
            )
        ]
    )

    reply_markup = InlineKeyboardMarkup(keyboard)

    message = (
        "🧠 *LIFEGUARD 365 SAFETY QUIZ*\n\n"
        f"*Question {question_index + 1} of "
        f"{len(QUIZ_QUESTIONS)}*\n\n"
        f"{question['question']}\n\n"
        "Choose the safest answer:"
    )

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


async def answer_quiz(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    """Process a quiz answer."""

    query = update.callback_query
    await query.answer()

    try:
        selected_answer = int(query.data.split(":")[1])
    except (ValueError, IndexError):
        await query.message.reply_text(
            "⚠️ Invalid quiz response."
        )
        return

    question_index = context.user_data.get("quiz_question", 0)

    if question_index >= len(QUIZ_QUESTIONS):
        return

    question = QUIZ_QUESTIONS[question_index]

    if selected_answer == question["answer"]:
        context.user_data["quiz_score"] = (
            context.user_data.get("quiz_score", 0) + 1
        )

        await query.message.reply_text(
            "✅ *Correct!*\n\n"
            "Excellent safety decision.",
            parse_mode="Markdown",
        )
    else:
        correct = question["options"][question["answer"]]

        await query.message.reply_text(
            "❌ *Not quite.*\n\n"
            f"The safest answer is:\n"
            f"✅ {correct}",
            parse_mode="Markdown",
        )

    context.user_data["quiz_question"] = question_index + 1

    await send_question(update, context)


async def finish_quiz(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    """Display the final quiz score."""

    score = context.user_data.get("quiz_score", 0)
    total = len(QUIZ_QUESTIONS)

    percentage = int((score / total) * 100)

    if percentage == 100:
        rating = "🏆 Excellent! Safety Champion!"
    elif percentage >= 80:
        rating = "🥇 Very Good! Strong safety awareness."
    elif percentage >= 60:
        rating = "🥈 Good! Keep improving."
    else:
        rating = "📚 Keep learning. Safety awareness saves lives."

    message = (
        "🏁 *QUIZ COMPLETED*\n\n"
        f"Your score: *{score}/{total}*\n"
        f"Percentage: *{percentage}%*\n\n"
        f"{rating}\n\n"
        "🛡️ Keep learning.\n"
        "💡 Stay alert.\n"
        "❤️ Protect life."
    )

    if update.callback_query:
        await update.callback_query.message.reply_text(
            message,
            parse_mode="Markdown",
        )
    else:
        await update.message.reply_text(
            message,
            parse_mode="Markdown",
        )

    context.user_data.pop("quiz_score", None)
    context.user_data.pop("quiz_question", None)


async def exit_quiz(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    """Exit the current quiz."""

    query = update.callback_query
    await query.answer()

    context.user_data.pop("quiz_score", None)
    context.user_data.pop("quiz_question", None)

    await query.message.reply_text(
        "🛡️ *QUIZ EXITED*\n\n"
        "No problem. You can start another safety quiz anytime.\n\n"
        "Stay safe. Protect life.",
        parse_mode="Markdown",
    )


# Compatibility aliases
quiz_start = start_quiz
quiz_answer = answer_quiz
