from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def index(request):
    return render(request, 'generator/home.html')


def password(request):
    letters = 'qwertyuiopsdfghjklzxcvbnm'
    uppper_case_letters = letters.upper()
    special_symbols = '!@#$%^&*()_+-=?></.,'
    numbers = '1234567890'
    if request.GET.get('uppercase'):
        letters += uppper_case_letters
    if request.GET.get('special'):
        letters += special_symbols
    if request.GET.get('numbers'):
        letters += numbers
    lenght = int(request.GET.get('lenght'))
    the_password = ''
    for password in range(lenght):
        the_password += random.choice(letters)





    return render(request, 'generator/password.html', {'password': the_password})
