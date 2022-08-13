# render html web pages
from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string
import random 

def home_view(request):
    num = random.randint(1,3)
    article = Article.objects.get(id=num)
    articles = Article.objects.all()

    context = {
        'articles': articles,
        'title': article.title,
        'content': article.content,
        'id': article.id
    }

    htmlpage = render_to_string('home_view.html', context=context)
    return HttpResponse(htmlpage)