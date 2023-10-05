# ATOMIC_HABITS

### _**SPA-application for DRF**_

The project allows you to track your habits and receive notifications by telegram bot

**Requirements:**\
celery
coverage
Django
django-celery-beat
django-cors-headers
django-filter
django-timezone-field
djangorestframework
djangorestframework-simplejwt
drf-yasg
flake8
psycopg2-binary
python-crontab
python-dotenv
pytz
requests

**.env**\
This application needs you to create ".env" file. Then you need to set all constants. For example, there is structure for ".env" file:
TG_BOT_TOKEN='example-telegram-bot-token'

**#Celery**\
CELERY_BROKER_URL = 'your://url:1234'
CELERY_RESULT_BACKEND = 'your://url:1234'
CELERY_TASK_TRACK_STARTED = True

**#Database**\
NAME = 'db_name'
USER = 'user_name'
PASSWORD = 'verysecretpassword'
