from django.urls import path
from articles.views import articlesView
from . import views
app_name = 'articles'
urlpatterns = [
    path('', articlesView.as_view(), name='article_list'),
    # path(r'^(P?<slug>[\w-]+)/$', editArticlesView.as_view(), name='details'),
    path('create', views.article_create, name='create'),
    path('<slug:slug>', views.article_details, name='details'),
]