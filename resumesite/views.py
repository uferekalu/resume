from django.shortcuts import render
from blog.models import BlogPost
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    queryset_list = BlogPost.objects.all().published()[:5]
    if request.user.is_authenticated:
        queryset_list = BlogPost.objects.all()
    
    paginator = Paginator(queryset_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        'blog_title': 'Welcome to My Blog List',
        'site_title': 'Details About The Site',
        'blog_list': queryset,
        'page_request_var': page_request_var
    }
    return render(request, 'resumesite/home.html', context)

def about(request):
    context = {}
    return render(request, 'resumesite/about.html', context)

def contact(request):
    context = {}
    return render(request, 'resumesite/contact.html', context)