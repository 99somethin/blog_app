from django.urls import path
from apps.articles import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='articles_index'),
    path('<int:id>/edit/', views.ArticleFormEditView.as_view(), name='articles_update'),
    path('<int:id>/', views.ArticleView.as_view(), name='articles_detail'),
    path('create/', views.CreateArticleView.as_view(), name='article_create'),
    path('<int:id>/delete/', views.DeleteArticleView.as_view(), name='aricle_delete'),
]