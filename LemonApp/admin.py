from django.contrib import admin
from .models import MenuItem, cat
# Register your models here.
admin.site.register(cat)
admin.site.register(MenuItem)