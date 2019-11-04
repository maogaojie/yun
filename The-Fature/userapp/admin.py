from django.contrib import admin
from django.contrib.sessions.models import Session
from userapp.models import User, UserInfo
# Register your models here.


admin.site.register(Session)
admin.site.register(User)
admin.site.register(UserInfo)
