from django.contrib import admin
from .models import Album, Song

# Register your models here so they may appear on http://127.0.0.1:8000/admin/
admin.site.register(Album)
admin.site.register(Song)