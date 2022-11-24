from service.constants.constants import TELEGRAM_GROUP_ID, TELEGRAM_SEND_MESSAGE_URL
import requests


class SendTelegramMessages:
    @staticmethod
    def send_telegram_message(chat_id, messages):
        param = {'chat_id': chat_id, 'text': messages}
        requests.get(TELEGRAM_SEND_MESSAGE_URL, params=param)
        return "True"
