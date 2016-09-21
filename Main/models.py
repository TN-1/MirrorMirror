from __future__ import unicode_literals
import datetime

from django.db import models

# Create your models here.

class CalendarItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date = models.DateField(editable=True, default=datetime.date.today())
    day = models.CharField(max_length=10)

    def __str__(self):
        s = str(self.date) + " - " + self.name
        return s

class Greetings(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content
