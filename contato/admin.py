from django.contrib import admin
from contato.models import Contato, Category

@admin.register(Contato)
# Register your models here.
class ContatoAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name0', 'phone', 'show',
    ordering = '-id',
   # list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name0',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'first_name', 'last_name0', 'show',
    list_display_links = 'id', 'phone',


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',
