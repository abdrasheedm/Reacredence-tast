from django.contrib import admin

# Register your models here.
from bills.models import Item

admin.site.register(Item)
