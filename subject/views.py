from multiprocessing.sharedctypes import Value
from urllib import response
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import pin_point,benefit,topic
# Create your views here.



def index(request):
    return HttpResponse("Hello, world. You're at the view index.")


def mail(request):
    sub=None
    cat = request.GET.get("category")
    if cat== "1":
        sub=benefit.objects.all()
    elif cat=="2":
        sub=topic.objects.all()
    elif cat=="3": 
        sub=pin_point.objects.all()       
      
    return render(request,'output.html',{
        'sub': sub,
        'catagory':cat
    })
