from django.contrib import admin
from .models import Tour, Story, Contact


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['header', 'description', 'price']


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['header', 'paragraph']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'message']