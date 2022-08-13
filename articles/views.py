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
