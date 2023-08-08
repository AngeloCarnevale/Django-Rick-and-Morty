from django.urls import path
from blog import views


app_name = 'blog'

# Django URLS;
# URL Dispatcher
# https://docs.djangoproject.com/en/4.2/topics/http/urls/

urlpatterns = [
    path('', views.blog, name='index'),
    path('<int:post_id>', views.post, name='post'),
]
