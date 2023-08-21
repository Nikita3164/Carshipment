from django.shortcuts import render
from .models import Car, News

# Create your views here.
def index(request):
    return render(request, 'main/main.html')


def setup(request):
    return render(request, 'main/classification.html')


def catalog(request):
    cars = Car.objects.all()
    return render(request, 'main/catalog.html', {'cars': cars})


def news(request):
    news = News.objects.all()
    return render(request, 'main/news.html', {'news': news})