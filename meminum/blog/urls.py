# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='home'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article/new/', views.ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('article/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('profile/', views.profile, name='profile'),
]