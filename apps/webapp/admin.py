from django.contrib import admin

# Register your models here.
from apps.webapp.models import Contact


admin.site.register(Contact)