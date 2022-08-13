# render html web pages
from django.http import HttpResponse
import random

def home_view(request):
    name = 'tomasito'
    num = random.randint(0,1000)
    h1_str = f"""
    <h1>Hello {name}!</h1>
    """
    p_str = f"""
    <p>{num} visits today</p>
    """
    htmlpage = h1_str + p_str
    return HttpResponse(htmlpage)