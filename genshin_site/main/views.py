from django.shortcuts import render
from .models import Characters

def main(request):
    hero = Characters.objects.all()
    return render(request,'main/home.html', {'hero' : hero})