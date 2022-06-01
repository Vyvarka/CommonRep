from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Topic)
admin.site.register(models.Entry)
admin.site.register(models.Article)
admin.site.register(models.Feedback)
