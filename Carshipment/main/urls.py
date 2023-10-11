from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('classification', views.setup),
    path('catalog', views.catalog, name='catalog'),
    path('news', views.news),
    path('model', views.model),
    path('contacts', views.contacts, name='contacts')
]