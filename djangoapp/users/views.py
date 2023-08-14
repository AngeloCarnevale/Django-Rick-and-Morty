from django.shortcuts import render, redirect
from django.http.response import HttpResponse  
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html', context= {'title':'Cadastro'})
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(username=username).first()
        
        if user:
            return HttpResponse("Usuário já cadastrado")
        
        else:
            user = User.objects.create_user(username, email, senha, is_staff=True)
            user.save()
            return redirect("/auth/login")


def userLogin(request):
    if request.method == "GET":
        return render(request, 'login.html', context={
            'title': 'Login'
        })
    
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha)
        
        if user:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("Erro")
            
