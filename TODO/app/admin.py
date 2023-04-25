from django.contrib import admin
from app.models import TODO
# Register your models here.
@admin.register(TODO)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'user','date']