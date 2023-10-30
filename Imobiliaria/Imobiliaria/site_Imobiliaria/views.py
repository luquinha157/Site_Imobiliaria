# Create your views here.
from django.shortcuts import render, redirect
from .models import *
from Website.forms import LoginEmail, Feedback, CadastrarLivros, CadastrarUsuario, ReservarLivros
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date
# Create your views here.

# ----------- Páginas
def index(request):
    return render(request, 'index.html')