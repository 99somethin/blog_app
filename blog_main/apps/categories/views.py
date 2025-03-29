from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.urls import reverse
from apps.categories.models import Category
from apps.categories.forms import CategoryForm

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
    

class CategoryCreate(View):
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        form = CategoryForm()
        return render(request, 'category_create.html', {
            'form': form
        })
    
    def post(self, request, *args, **kwargs):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('categories_index'))
        else:
            return render(request, 'create.html', {
            'form': form
        })

            
    
