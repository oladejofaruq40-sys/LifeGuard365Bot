import logging
from telegram.ext import Application, 
ContextTypes
from database.database import get_subscribers
from services.safety_content import 
get_daily_safety_message
logger = logging.getLogger(__name__)
async def send_daily_safety_message(
    context: ContextTypes.DEFAULT_TYPE
):
    """
    Sends today's safety message to every active 
subscriber.
    """
    message = get_daily_safety_message()
    subscribers = get_subscribers()
    logger.info(
        "Sending daily safety message to %s 
subscribers",
        len(subscribers)
    )
    successful = 0
    failed = 0
    for user_id in subscribers:
        try:
            await context.bot.send_message(
                chat_id=user_id,
                text=message,
                parse_mode="Markdown",
            )
            successful += 1
        except Exception as error:
            failed += 1
            logger.warning(
                "Could not send message to %s: %s",
                user_id,
                error
            )
    logger.info(
        "Daily broadcast completed. "
        "Successful: %s | Failed: %s",
        successful,
        failed
    )
def setup_scheduler(application: Application):
    job_queue = application.job_queue
    if job_queue is None:
        raise RuntimeError(
            "Telegram JobQueue is not available. "
            "Check the python-telegram-bot 
dependencies."
        )
    # 7:00 AM every day
    from datetime import time
    from zoneinfo import ZoneInfo
    daily_time = time(
        hour=7,
        minute=0,
        tzinfo=ZoneInfo("Africa/Lagos")
    )
    job_queue.run_daily(
        send_daily_safety_message,
        time=daily_time,
        name="daily_safety_broadcast",
    )
    logger.info(
        "Daily LifeGuard 365 broadcast scheduled for 
07:00 Africa/Lagos."
    )