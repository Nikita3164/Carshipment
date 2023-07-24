from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('classification', views.setup),
    path('catalog', views.catalog),
]