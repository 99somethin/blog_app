from django.urls import include, path
from apps.main_page import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
