import requests

from config.settings import TELEGRAM_API
from users.models import User

tg_token = TELEGRAM_API


def send_message(username, text):
    updates = get_updates()
    if updates['ok']:
        parse_updates(updates['result'])

    chat_id = User.objects.get(telegram=username).chat_id
    if not chat_id:
        print('Can not get user chat ID')
        return

    data_for_request = {
        'chat_id': chat_id,
        'text': text
    }

    response = requests.get(
        f'https://api.telegram.org/bot{tg_token}/sendMessage', data_for_request
    )
    return response.json()


def get_updates():
    response = requests.get(
        f'https://api.telegram.org/bot{tg_token}/getUpdates'
    )
    return response.json()


def parse_updates(updates):
    print(updates)
    for u in updates:
        user = User.objects.get(telegram=u['message']['chat']['username'])
        if User.objects.filter(telegram=user).exists():
            user.chat_id = u['message']['chat']['id']
            user.update_id = u['update_id']
            user.save()
