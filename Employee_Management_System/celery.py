import os

from celery import Celery
from scrape import break_login_logout
from Ems.Log import logged
from skpy import *
from Employee_Management_System import settings
from Ems.models import *


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Employee_Management_System.settings')

app = Celery('Employee_Management_System')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Hello from celery')


@app.task()
def log_task():
    sk = Skype(settings.SKYPE_EMAIL, settings.SKYPE_PASS)
    print("celery function")
    log_time = break_login_logout()
    for i in log_time:

        if i.content.lower() == logged.get('Break'):
            a = str(i)
            b = a.split("UserId")[1].strip()[1:].strip().split("ChatId:")[0].strip()
            date = a.split("Time")[1].split()[1:2]
            time = str(a.split("Time")[1].split()[2:3])
            time = time[2:10]
            contact = sk.contacts[b]
            name = contact.name
            print("name    ", name)
            obj = Employee.objects.get(name=name)

            log = Log_status.objects.create(Emp=obj, Log="break", Time=time)
            log.save()

            logged_time = Logged_Time.objects.create(Employee=obj, Date=date[0])
            logged_time.Log.add(log)

        if i.content.lower().replace(" ", "") == logged.get('Login'):
            a = str(i)
            b = a.split("UserId")[1].strip()[1:].strip().split("ChatId:")[0].strip()
            date = a.split("Time")[1].split()[1:2]
            time = str(a.split("Time")[1].split()[2:3])
            time = time[2:10]
            contact = sk.contacts[b]
            name = contact.name
            print("name    ",name)
            obj1 = Employee.objects.get(name=name)

            log = Log_status.objects.create(Emp=obj1, Log="login", Time=time)
            log.save()

            logged_time = Logged_Time.objects.create(Employee=obj1, Date=date[0])
            logged_time.Log.add(log)

        if i.content.lower().replace(" ", "") == logged.get('Back_to_work'):
            a = str(i)
            b = a.split("UserId")[1].strip()[1:].strip().split("ChatId:")[0].strip()
            date = a.split("Time")[1].split()[1:2]
            time = str(a.split("Time")[1].split()[2:3])
            time = time[2:10]
            contact = sk.contacts[b]
            name = contact.name
            obj2 = Employee.objects.get(name=name)

            log = Log_status.objects.create(Emp=obj2, Log="back to work", Time=time)
            log.save()

            logged_time = Logged_Time.objects.create(Employee=obj2, Date=date[0])
            logged_time.Log.add(log)

        if logged.get('Logout') in i.content.lower():
            a = str(i)
            b = a.split("UserId")[1].strip()[1:].strip().split("ChatId:")[0].strip()
            date = a.split("Time")[1].split()[1:2]
            time = str(a.split("Time")[1].split()[2:3])
            time = time[2:10]
            contact = sk.contacts[b]
            name = contact.name
            obj3 = Employee.objects.get(name=name)

            log = Log_status.objects.create(Emp=obj3, Log="logout", Time=time)
            log.save()

            logged_time = Logged_Time.objects.create(Employee=obj3, Date=date[0])
            logged_time.Log.add(log)


@app.task(bind=True)
def debug_task2(self):
    print(f'Request: {self.request!r}')