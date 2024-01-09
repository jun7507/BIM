from django.urls import path
from . import views

urlpatterns = [
    # base
    path('', views.base, name='base'),
]