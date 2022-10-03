from django.contrib import admin
from .models import TodoList, Item
# Register your models here.
# Need to "register these" to make them visible in the 
# Admin dashboard
admin.site.register(TodoList)
admin.site.register(Item)


