from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/main.html')


def setup(request):
    return render(request, 'main/classification.html')


def catalog(request):
    return render(request, 'main/catalog.html')