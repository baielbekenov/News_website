from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect
from django.views import generic

from .forms import NewsCreateForm, PostsDetailForm
from .models import News, Categories, Posts, MakepostCat, Article


def index(request):
    news = News.objects.all()
    posts = Posts.objects.all()
    cat_info = MakepostCat.objects.all()
    return render(request, 'index.html', locals())

def index2(request):
    articles = Article.objects.all()
    return render(request, 'elements.html', locals())


class DetailBookView(generic.DetailView):
    template_name = 'detail.html'
    model = News
    context_object_name = 'new'

    def get_success_url(self):
        return reverse('index')


class CreateBookView(generic.ListView):
    template_name = 'generic.html'
    model = News
    context_object_name = 'new'

    def get_success_url(self):
        return reverse('index')

class Elements(generic.ListView):
    template_name = 'elements.html'
    model = News
    context_object_name = 'new'

    def get_success_url(self):
        return reverse('index')


def list_category(request):
    categories = Categories.objects.all()
    return render(request, 'generic.html', {'categories': categories})


# class ListCategory(generic.DetailView):
#     template_name = 'list_category'
#     model = Categories
#     context_object_name = 'category'
#
#
#     def get_queryset(self):
#         object = self.get_object()
#
#     def get_success_url(self):
#         return reverse('generic')


class NewsCreateView(generic.CreateView):
    template_name = 'create.html'
    form_class = NewsCreateForm
    model = News

    def get_success_url(self):
        return reverse('index')


class PostDetailView(generic.DetailView):
    template_name = 'posts_detail.html'
    # form_class = PostsDetailForm
    model = Posts
    context_object_name = 'poss'

    def get_success_url(self):
        return reverse('index')



# def index2(request):
#     cat_info = MakepostCat.objects.all()
#     return render(request, 'generic.html', locals())


class ListCategory(generic.DetailView):
    template_name = 'list_category.html'
    model = Categories
    context_object_name = 'category'

    def get_success_url(self):
        return reverse('list_categories')