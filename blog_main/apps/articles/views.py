from django.shortcuts import get_object_or_404, render
from django.views import View
from apps.articles.models import Article

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