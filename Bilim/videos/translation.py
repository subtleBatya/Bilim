from modeltranslation.translator import register, TranslationOptions
from .models import Video_course, Video_category


@register(Video_category)
class Video_categoryTranslateOptions(TranslationOptions):
    fields = ("category_name",)


@register(Video_course)
class Video_course(TranslationOptions):
    fields = ("course_name",)