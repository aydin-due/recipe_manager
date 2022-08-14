from django.shortcuts import render
from .models import Article

# Create your views here.
def article_detail_view(request, id=None):
    article = None
    if id:
        article = Article.objects.get(id=id)
    context = {
        'article': article
    }
    return render(request, 'articles/details.html', context=context)

def article_search_view(request):
    # print(dir(request))
    query_dict = request.GET
    article = None
    try:
        query = int(query_dict.get("q"))
    except:
        query = None
    if query:
        article = Article.objects.get(id=query)
    context = {
        'article': article
    }
    return render(request, 'articles/search.html', context=context)