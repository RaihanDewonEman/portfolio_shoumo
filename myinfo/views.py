from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.

def Homepage(request):
    return render(request, 'myinfo/home.html', {'name': 'Home Page'})