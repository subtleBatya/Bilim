from modeltranslation.translator import register, TranslationOptions
from .models import Scientist


@register(Scientist)
class ScientistTranslationOptions(TranslationOptions):
    fields = ("scientist_name", "scientist_text")