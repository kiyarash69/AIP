from django.contrib import admin
from .models import *

All = [
    OurService,
    WhyAi,
]

admin.site.register(All)
