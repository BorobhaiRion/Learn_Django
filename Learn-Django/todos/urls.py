from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('', views.new, name='new'),
    path('html', views.html, name='html'),
    path('index/<str:name>', views.index, name='index'),
    path('sum/<int:a>/<int:b>', views.sum, name='sum'),
    path('special', views.special, name='special')
]