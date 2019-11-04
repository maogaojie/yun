from django.contrib import admin
from fileapp import models
# Register your models here.

admin.site.register(models.Storage)
admin.site.register(models.MIMEType)
admin.site.register(models.File)
admin.site.register(models.Share)
admin.site.register(models.Liked)
