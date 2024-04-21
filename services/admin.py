from django.contrib import admin
from .models import *

All = [
    Service,
    InnovationModel,
]

admin.site.register(All)
