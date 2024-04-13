from django.contrib import admin
from .models import *

All = [
    OurService,
    WhyAi,
    DailyNews,
]

admin.site.register(All)
