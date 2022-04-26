# from django import template
# import colorama
# from colorama import Fore

from django.shortcuts import render,redirect
from django.http import HttpResponse
# from .forms import inputForm
from .models import pin_point,benefit,topic
# Create your views here.

# register = template.Library()


def index(request):
    return HttpResponse("Hello, world. You're at the view index.")
 
def mail(request):
    sub=None
    sentance=None
    # form=inputForm(request.GET or None)
    inp=request.GET.get("word")
    cat = request.GET.get("category")
    # inp2= Fore.RED + inp
    # print(inp2)
    if request.method=='GET':
        print("getted")
        # if form.is_valid():
        #     print("valid")
        if cat== "1":
            sub=benefit.objects.all()
            for s in sub:
                sentance= s.title.replace("{}",inp)
                s.title=sentance
        elif cat=="2":
            sub=topic.objects.all()
            for s in sub:
                sentance= s.title.replace("{}",inp)
                s.title=sentance
        elif cat=="3": 
            sub=pin_point.objects.all() 
            for s in sub:
                sentance= s.title.replace("{}",inp)
                s.title=sentance     
      
    return render(request,'output.html',{
        'sub': sub,
        'catagory':cat,
        'sentance':sentance,
        'inp':inp
    })
