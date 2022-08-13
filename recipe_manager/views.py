# render html web pages
from django.http import HttpResponse
from articles.models import Article
import random 

def home_view(request):

    num = random.randint(1,3)
    article = Article.objects.get(id=num)

    context = {
        'title': article.title,
        'content': article.content,
        'id': article.id
    }

    htmlpage = """
    <h1>{title} (id: {id})</h1>
    <p>{content}</p>
    """.format(**context)
    return HttpResponse(htmlpage)