from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
     return render(request,'tamplates/generator/home.html')

def pasword(request):
    thepasword = ''
    len = request.GET.get('lenght',12)
    character = list('qwertyuiopasdfghjklzxcvbnm')
    
    if request.GET.get('uppercase'):
        character.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('nambers'):
        character.extend(list('1234567890'))
    if request.GET.get('special'):
        character.extend(list('!@#$%^&*()_'))
    for i in range(int(len)):
        thepasword += random.choice(character)
    return render(request,'tamplates/generator/pasword.html',{'pasword':thepasword})

def opisanie(request):
    return render(request,'tamplates/generator/opisanie.html')