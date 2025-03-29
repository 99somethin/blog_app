from django.shortcuts import get_object_or_404, render
from django.views import View
from apps.categories.models import Category


class IndexView(View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, 'templates/index.html', context={
            'categories': categories,
        })



class ViewID(View):
    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, id=kwargs['id'])
        
        articles = category.article_set.all()
        
        return render(request, 'templates/category.html', context={
            'category': category,
            'articles': articles
        })
