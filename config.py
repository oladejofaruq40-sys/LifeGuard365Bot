import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

BOT_NAME = "LifeGuard365"

BOT_VERSION = "1.0.0"

TIMEZONE = "Africa/Lagos"

DAILY_POST_TIME = "07:00"
