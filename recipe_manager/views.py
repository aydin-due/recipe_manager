# render html web pages

from django.http import HttpResponse

htmlpage = """
<h1>Hello World</h1>
"""

def home(request):
    return HttpResponse(htmlpage)