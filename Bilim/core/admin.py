from django.contrib import admin
from .models import Scientist

class ScientistAdmin(admin.ModelAdmin):
    list_display = ("scientist_name", "scientist_text")

admin.site.register(Scientist, ScientistAdmin)