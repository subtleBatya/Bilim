from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Video_category
@receiver(post_migrate)
def precreate_models(sender, **kwargs):
    if sender.name == "videos":
        video_categories = [
            {"name":"Гуманитарные курсы"},
            {"name":"Технические курсы"},
            {"name":"Естественные курсы"}
        ]

        for cat in video_categories:
            Video_category.objects.get_or_create(category_name=cat["name"])

