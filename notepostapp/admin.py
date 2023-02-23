from django.contrib import admin
from .models import Notepost

class NotepostAdmin(admin.ModelAdmin):
    list_display = ('text', 'user')

admin.site.register(Notepost, NotepostAdmin)
