from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('<str:code>/', views.decode_view, name='decode'),
]