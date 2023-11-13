from django.contrib import admin
from .models import Note, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'f_name', 'l_name', 'password')
    list_display = ('id', 'username', 'full_name', 'registrate_date')
    list_display_links = ('id', 'username')


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    fields = ('user', 'category', 'reason', 'price')
    list_display = ('id', 'user', 'category', 'reason', 'price', 'date_time')
    list_display_links = ('id', 'user', )
