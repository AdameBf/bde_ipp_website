from django.contrib import admin

# Register your models here.
from .models import Buddy, Buddlunteer

admin.site.register(Buddy)
admin.site.register(Buddlunteer)