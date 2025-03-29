from django.urls import path
from apps.categories import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='categories_index'),
    path('<int:id>/', views.ViewID.as_view(), name='categories_id'),
    path('create/', views.CategoryCreate.as_view(), name='category_create'),
]