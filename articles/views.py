from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Article
from .forms import ArticleForm

# Create your views here.
def article_detail_view(request, slug=None):
    article = None
    if slug:
        try:
            article = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article = Article.objects.filter(slug=slug).first()
        except:
            raise Http404
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

# @csrf_exempt override security rules
@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None) # acts as a get method, value is None if there's no request.POST
    context = {
        'form': form
    }
    if form.is_valid():
        article = form.save()
        context['form'] = ArticleForm() #cleans out form after it's posted
        # title = form.cleaned_data.get("title")
        # content = form.cleaned_data.get("content")
        # article = Article.objects.create(title=title, content=content)
        # context['article'] = article
        # context['created'] = True
    return render(request, 'articles/create.html', context=context)