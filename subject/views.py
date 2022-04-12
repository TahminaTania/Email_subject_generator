# from django import template
# import colorama
# from colorama import Fore

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import pin_point,benefit,topic
# Create your views here.

# register = template.Library()


def index(request):
    return HttpResponse("Hello, world. You're at the view index.")
 
def mail(request):
    sub=None
    cat = request.GET.get("category")
    word=None
    inp=request.GET.get("word")
    # inp2= Fore.RED + inp
    # print(inp2)
    
    if cat== "1":
        sub=benefit.objects.all()
        for s in sub:
            word= s.title.replace("{}",inp)
            s.title=word
    elif cat=="2":
        sub=topic.objects.all()
        for s in sub:
            word= s.title.replace("{}",inp)
            s.title=word
    elif cat=="3": 
        sub=pin_point.objects.all() 
        for s in sub:
            word= s.title.replace("{}",inp)
            s.title=word      
      
    return render(request,'output.html',{
        'sub': sub,
        'catagory':cat,
        'word':word,
        'inp':inp
    })
