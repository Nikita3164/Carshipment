from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('classification', views.setup),
    path('catalog', views.catalog, name='catalog'),
    path('news', views.news),
    path('model', views.model),
    path('contacts', views.contacts, name='contacts'),
    path('promotion', views.promotion, name='promotion'),
    path('privacy', views.privacy),
    path('agreement', views.agreement),
    path('security', views.security)
]