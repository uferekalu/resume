from django.shortcuts import render
from blog.models import BlogPost
from records.models import Details
from .models import SearchQuery

# Create your views here.
def search_view(request):
    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context = {
        'query': query
    }   
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        blog_list = BlogPost.objects.search(query=query)
        detail_list = Details.objects.search(query=query)
        context['blog_list'] = blog_list
        context['detail_list'] = detail_list
    return render(request, 'searches/view.html', context)