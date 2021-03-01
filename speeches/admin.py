from django.contrib import admin

# Register your models here.

from .models import Speaker, Speech 

admin.site.register(Speaker)
admin.site.register(Speech)