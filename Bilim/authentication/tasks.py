from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_custom_email(toemail, subject, html_message):
    try:
        send_mail(
            subject, 
            "",  # Plain text version (optional)
            settings.EMAIL_HOST_USER,   
            recipient_list=toemail,
            fail_silently=False,
            html_message=html_message  # Send as HTML
        )
        print("Successfully sent email")
    except Exception as e:
        print(f"Failed to send email: {e}")
