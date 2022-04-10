from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import subject
# Create your views here.



def index(request):
    return HttpResponse("Hello, world. You're at the view index.")


def mail(request):
    sub=subject.objects.all()
    return render(request,'output.html',{
        'sub': sub
    })
