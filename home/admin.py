from django.contrib import admin
from .models import *

All = [
    OurService,
    WhyAi,
    DailyNews,
    Profile,
    ContactModel,
]

admin.site.register(All)
