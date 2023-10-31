from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from site_Imobiliaria.forms import LoginForms, RegisterForms, MessageSend
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    user = User.objects.all()
    form = RegisterForms()
    return render(request, 'index.html', {'users': user, 'form':form})

def dashboard(request):
    return render(request, "dashboard.html")

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            email = form['email'].value()
            password = form['senha'].value()
        user_temp = User.objects.get(email= email)

        user = auth.authenticate(
            request,
            username=user_temp,
            password=password
        )

        if user is not None:
            auth.login(request, user)
            messages.success(request, f'Foi logado com sucesso!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})

def properties(request):
    return render(request, "properties.html")

def messageEnviar(request):
    if request.method == 'POST':
        form_Message = MessageSend(request.POST)

        if form_Message.is_valid():
            Message.objects.create(
            nome = form_Message['nome_form'].value(),
            email = form_Message['email_form'].value(),
            subject = form_Message['subject_form'].value(),
            message = form_Message['message_form'].value(),
            )
            messages.success(request, f'Usuário cadastrado com sucesso!')

            return redirect('index.html')
    else:
        form_Message = MessageSend

        return render('index.html',{'form_Message':form_Message})