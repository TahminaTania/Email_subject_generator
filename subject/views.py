# from django import template
# import colorama
# from colorama import Fore


from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
# from .forms import inputForm
from .models import pin_point, benefit, topic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def mail(request):
    sub = None
    sentance = None
    if request.method == 'GET':
        inp = request.GET.get("word")
        cat = request.GET.get("category")
        print("getted")
        if cat and inp:
            if cat == "Benefit":
                sub = benefit.objects.all()
            elif cat == "Topic":
                sub = topic.objects.all()
            elif cat == "Pain-Point":
                sub = pin_point.objects.all()

            for s in sub:
                sentance = s.title.replace("{}", inp)
                s.title = sentance

    return render(request, 'output.html', {
        'sub': sub,
        'catagory': cat,
        'sentance': sentance,
        'inp': inp,
    })
