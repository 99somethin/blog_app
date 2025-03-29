from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import View
from apps.articles.models import Article
from apps.articles.forms import ArticleForm

class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return render(request, 'templates/categories_index.html', context={
            'articles': articles,
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'templates/article.html', context={
            'article': article,
        })
    

class CreateArticleView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('articles_index'))  
        else:
            return render(request, 'articles/create.html', {'form': form})
        

class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'article_update.html', {'form': form, 'article_id': article_id})
    
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles_index')

        return render(request, 'article_update.html', {'form': form, 'article_id':article_id})
    

class DeleteArticleView(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect(reverse('articles_index'))