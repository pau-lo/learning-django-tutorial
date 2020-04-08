from django.urls import path
from .views import HomePageView, AboutPageView, ArticleDetailView, ArticleCreateView

urlpatterns = [
    path('article/new/', ArticleCreateView.as_view(),
         name='add_article'),
    path('article/<int:pk>/', ArticleDetailView.as_view(),
         name='article_detail'),
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
]
