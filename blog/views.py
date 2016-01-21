from django.shortcuts import render

from django.shortcuts import render_to_response, get_object_or_404, render
from .models import Article
from django.template.defaultfilters import title

# Create your views here.
def IndexView(request):
    articles = Article.objects.all()
    return render_to_response('index.html',{'articles_2':articles[:2],'articles_5':articles[:5]})

def InformationView(request):
    return render_to_response('information.html')

def DetailView(request,article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render_to_response('subpage.html',{'article':article})