from django.contrib import admin
from apps.articles.models import Article

# Register your models here.
class AdminArticle(admin.ModelAdmin):
    list_display = ('title', 'body')  
    search_fields = ('title', 'content')   


admin.site.register(Article, AdminArticle)

