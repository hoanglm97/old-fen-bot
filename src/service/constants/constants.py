import os
from dotenv import load_dotenv

load_dotenv()

BETS_API_TOKEN = os.environ.get("BETS_API_TOKEN")
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_GROUP_ID = os.environ.get("TELEGRAM_GROUP_ID")
TELEGRAM_SEND_MESSAGE_URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
