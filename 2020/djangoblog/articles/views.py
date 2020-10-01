from django.shortcuts import render, redirect
from django.views import View
from .models import Article;
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
class articlesView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all().order_by("date");
        # return HttpResponse("its index page");
        return render(request, 'articles/article_list.html', {'articles':articles})
# class editArticlesView(View):
#     def get(self, request, slg, *args, **kwargs):
#         article = Article.objects.get(slug=slg)
#         print(article)
        # return HttpResponse("its index page");
        # return render(request, 'articles/article_details.html', {'article':article});
def article_details(request, slug):
     article = Article.objects.get(slug=slug)
     print(article.body)
        # return HttpResponse("its index page");
     return render(request, 'articles/article_details.html', {'article':article});

@login_required(login_url="/accounts/login/")
def article_create(request):
        if request.method == 'POST':
                form = forms.CreateArticle(request.POST, request.FILES);
                if form.is_valid():
                        instance = form.save(commit=False)
                        instance.author = request.user
                        instance.save();
                        return redirect('articles:article_list')
        else:
                form = forms.CreateArticle();
                return render(request, 'articles/article_create.html', {'form':form})

