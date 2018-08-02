from django.contrib import admin
from spiders import models
# Register your models here.
admin.site.register(models.Spider)
admin.site.register(models.Result)