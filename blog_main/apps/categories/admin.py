from django.contrib import admin
from apps.categories.models import Category

# Register your models here.

class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'description')  
    search_fields = ('name', 'description')   


admin.site.register(Category, AdminCategory)
