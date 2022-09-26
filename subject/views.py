# from django import template
# import colorama
# from colorama import Fore


from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from .models import pin_point, benefit, topic
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
# Create your views here.


def registerPage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('log')

    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)


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
