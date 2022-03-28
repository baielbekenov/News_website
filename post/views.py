from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect
from django.views import generic
from .models import News


def index(request):
    news = News.objects.all()

    return render(request, 'index.html', locals())


class DetailBookView(generic.DetailView):
    template_name = 'detail.html'
    model = News
    context_object_name = 'new'

    def get_success_url(self):
        return reverse('index')


class CreateBookView(generic.CreateView):
    template_name = 'generic.html'
    model = News
    context_object_name = 'new'

    def get_success_url(self):
        return reverse('index')

