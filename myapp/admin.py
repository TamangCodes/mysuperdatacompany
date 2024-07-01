from django.contrib import admin
from .models import uploadFile



@admin.register(uploadFile)
class UploadedFileAdmin(admin.ModelAdmin):
    pass