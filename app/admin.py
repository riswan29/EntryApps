from django.contrib import admin
from .models import *
# Register your models here.


class userPROF(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)

admin.site.register(UserProfile, userPROF)
