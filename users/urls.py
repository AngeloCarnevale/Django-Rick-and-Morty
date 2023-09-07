from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
]
