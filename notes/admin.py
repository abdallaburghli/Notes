from django.contrib import admin

# Register your models here.

from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('id','text','owner')
    list_display_links = ('id','text')
    list_per_page = 25


admin.site.register(Note,NoteAdmin)