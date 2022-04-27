from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = 'full_description'
    list_display = ('id', 'title', 'category', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('is_published', 'category')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published',)

admin.site.register(Category, AdminCategory)
admin.site.register(Product, SummerAdmin)
admin.site.register(Phone)
