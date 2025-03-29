from django.forms import ModelForm
from apps.articles.models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Здесь можно добавить кастомные виджеты или стили. Например, добавим CSS классы.
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['body'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
