from django.contrib import admin
from .models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "telephone_number")
    list_filter = ("username",)

admin.site.register(User, UserAdmin)


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("username", "subscription_start_date", "subscription_end_date")

admin.site.register(subscription, SubscriptionAdmin)

admin.site.register(User_abilities)
admin.site.register(UserRecentVideo)