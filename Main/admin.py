from django.contrib import admin
from .models import Greetings, CalendarItem
# Register your models here.

admin.site.register(Greetings)
admin.site.register(CalendarItem)
