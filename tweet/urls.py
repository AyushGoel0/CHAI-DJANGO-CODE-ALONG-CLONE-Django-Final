from django.urls import path
from . import views

app_name = 'tweet'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.tweet_list, name='list'),
    path('create/', views.tweet_create, name='create'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name='delete'),
    path('<int:tweet_id>/like/', views.tweet_like, name='like'),
]