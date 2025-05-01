from celery import shared_task
from .models import *

@shared_task
def delete_all_videos():
    lessons, chats, groups = New_lesson.objects.all(), ChatMessage.objects.all(), Group_chat.objects.all()
    try:
        lessons.delete()
        chats.delete()
        groups.delete()
        print("All deleted")
    except Exception as e:
        print(f"Error: {e}")