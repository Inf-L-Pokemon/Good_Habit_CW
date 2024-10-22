import requests
from celery import shared_task
from django.conf import settings
from datetime import datetime, timedelta
from habits.models import Habit


@shared_task
def telegram_notification():
    current_time = datetime.now()

    start_time = current_time + timedelta(minutes=5)
    end_time = start_time + timedelta(minutes=5)

    habits = Habit.objects.filter(time__gte=start_time.time(), time__lt=end_time.time())

    for habit in habits:
        chat_id = habit.owner.tg_chat_id
        if chat_id:
            message = f"Я буду {habit.action} в {habit.time} в {habit.place}"
            send_telegram_message.delay(chat_id, message)


@shared_task
def send_telegram_message(chat_id, message):
    params = {
            'text': message,
            'chat_id': chat_id
        }

    url = f'{settings.TELEGRAM_URL}{settings.TELEGRAM_BOT_TOKEN}/sendMessage'
    response = requests.get(url, params=params, timeout=10)
    if not response.ok:
        raise RuntimeError(f"Failed to sent telegram message to chat_id: {chat_id}")
