# from django import template
# import colorama
# from colorama import Fore


from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
# from .forms import inputForm
from .models import pin_point, benefit, topic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
# Create your views here.


def mail(request):
    sub = None
    sentance = None
    inp = request.POST.get("word")
    cat = request.POST.get("category")
    if request.method == 'POST':
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


# notes:
# if we do this with get data, urls will generate a csrf token, and input url, so if we want to ignore the url change we have to do it with POST.
# https://anshu-dev.medium.com/how-to-load-more-data-on-a-button-click-in-django-e1bab3a08e2b
