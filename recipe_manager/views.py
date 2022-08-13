# render html web pages
from django.http import HttpResponse
from articles.models import Article
import random 

def home_view(request):

    num = random.randint(1,3)
    article1 = Article.objects.get(id=num)

    h1_str = f"""
    <h1>{article1.title}</h1>
    """
    p_str = f"""
    <p>{article1.content}</p>
    """
    htmlpage = h1_str + p_str
    return HttpResponse(htmlpage)