from django.contrib import admin
from .models import User, Book, BookRecord
from import_export.admin import ImportExportModelAdmin

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    search_fields = ['title', 'author']
    list_display = ['title', 'author', 'count']
    list_filter = ['author']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']
    list_display = ['first_name', 'role']
    list_filter = ['role']


@admin.register(BookRecord)
class BookRecordAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'took_on']
    list_filter = ['user']
    autocomplete_fields = ['book', 'user']
    list_select_related = ['book', 'user']