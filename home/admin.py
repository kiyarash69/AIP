from django.contrib import admin
from .models import *

All = [
    OurService,
    WhyAi,
    DailyNews,
    Profile,

]

admin.site.register(All)
