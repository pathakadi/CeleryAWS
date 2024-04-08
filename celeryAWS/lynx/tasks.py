from celery import shared_task
from time import sleep
from django.core.mail import send_mail

@shared_task
def sleeptime(total_time):
    sleep(total_time)
    return None

@shared_task
def send_email_task():
    sleep(15)
    send_mail(
        "Celery Task Success" ,
        "This is a Test Message" ,
        "" ,
        [""] ,
    )
    return None