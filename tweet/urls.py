from django.urls import path
from . import views

app_name = 'tweet'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:tweet_id>/delete/', views.delete, name='delete'),
    path('<int:tweet_id>/like/', views.like, name='like'),
]