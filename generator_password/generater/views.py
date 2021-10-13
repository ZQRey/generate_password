from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return  render(request, 'generator/about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    lenght = int(request.GET.get('lenght', 12))
    if request.GET.get('uppercase'):
        characters.extend('ABCDFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('special'):
        characters.extend(r'~!@#$%^&*()_+<>?:"{}|[]\';/.,')
    if request.GET.get('numbers'):
        characters.extend('0123456789')
    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})
