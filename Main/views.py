import random, datetime
from datetime import timedelta
from pyowm import OWM
from models import Greetings, CalendarItem
from django.shortcuts import render

API_key = "792cb75dd2e7683a44997bedf8acc0e0"

def index(request):
    events = CalendarItem.objects.filter(date__range=[datetime.date.today(), (datetime.date.today() + timedelta(days=5))])
    events = events.order_by("date")
    i = 0
    while events.count() < 5:
        iday = datetime.date.today() + timedelta(days=i)
        try:
            if events[i].day != iday.strftime("%A"):
                CalendarItem.objects.create(name="", date=iday, day=iday.strftime("%A"))
            i = i + 1
        except:
            CalendarItem.objects.create(name="", date=iday, day=iday.strftime("%A"))
            events = CalendarItem.objects.filter(
                date__range=[datetime.date.today(), (datetime.date.today() + timedelta(days=5))])
            events = events.order_by("date")
            i = 0

    events = CalendarItem.objects.filter(date__range=[datetime.date.today(), (datetime.date.today() + timedelta(days=5))])
    events = events.order_by("date")

    owm = OWM(API_key)
    obs = owm.weather_at_id(2078025)
    w = obs.get_weather()
    weather = w.get_weather_code()
    temp = w.get_temperature('celsius')
    temp = round(temp['temp'], 0)
    greeting = random.choice(Greetings.objects.all())
    return render(request, 'Main/index.html', {'greeting': greeting, 'weather':weather, 'temp':temp, 'events':events})