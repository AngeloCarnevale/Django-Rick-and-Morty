from django.urls import path
from characters import views


app_name = 'characters'

# Django URLS;
# URL Dispatcher
# https://docs.djangoproject.com/en/4.2/topics/http/urls/

urlpatterns = [
    path('', views.characters, name='index'),
    path('<int:post_id>', views.character, name='character'),
]
