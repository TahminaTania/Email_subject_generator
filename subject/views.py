from django import template
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import pin_point,benefit,topic
# Create your views here.

# register = template.Library()


def index(request):
    return HttpResponse("Hello, world. You're at the view index.")


# @register.filter
# def to_and(value):
#     return value.replace("{}","and")
    
def mail(request):
    sub=None
    cat = request.GET.get("category")
    word=None
    inp=request.GET.get("word")
    
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
