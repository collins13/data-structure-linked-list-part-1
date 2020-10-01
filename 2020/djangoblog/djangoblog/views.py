from django.http import HttpResponse
from django.views import View
from django.shortcuts import render


class MyView(View):
    def get(self, request, *args, **kwargs):
        # return HttpResponse("hello world");
        return render(request, 'about.html')

class indexView(View):
    def get(self, request, *args, **kwargs):
        # return HttpResponse("its index page");
        return render(request, 'homepage.html')