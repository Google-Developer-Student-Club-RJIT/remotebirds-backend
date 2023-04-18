from __future__ import absolute_import
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'remotebirds.settings')
import django
django.setup()
from celery import Celery
from django.conf import settings




app = Celery('remotebirds')
app.conf.enable_utc = False

app.conf.update(timezone= "Asia/Kolkata")
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# from API.tasks import process_tweets_task
# Celery Beat Settings
app.conf.beat_schedule = {
    'celery-beat-tweet-task': {
        'task': 'API.tasks.process_tweets_task',
        'schedule': 60.0,
        #'args': (2,)
    }
    
}




@app.task(bind=True)
def debug_task(self):
    print(f'Request: {format(self.request)}')




