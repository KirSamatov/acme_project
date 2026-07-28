from django.contrib import admin

from .models import Birthday, Tag


@admin.register(Birthday)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'birthday'
    ]
    search_fields = ['first_name']

@admin.register(Tag)
class CategoryAdmin1(admin.ModelAdmin):
    list_display = [
        'tag',
    ]
    search_fields = ['tag']
