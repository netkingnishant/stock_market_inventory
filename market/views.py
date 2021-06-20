from collections import namedtuple

from django.http import HttpResponse
from django.contrib.auth import authenticate, login as loginUser, logout
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
from django.shortcuts import render, redirect
import requests, itertools
import json

from market.forms import marketForm
from market.models import market
from django.contrib.auth.decorators import login_required

offset = 0
count = 0

@login_required(login_url='signin')
def home(request):
    global count
    count += 1

    if not request.user.is_authenticated:
        user = request.user
        return redirect("signin")
    else:
        base_url = "https://sandbox.iexapis.com/v1/stock/market/batch?&types=quote&symbols=aapl,fb,tsla,tcs,ccne,agi,agl,agx,ahc,air&token=Tsk_3749e680bb284c1c9ac218f051ff8e26"
        data = requests.get(base_url)

        if data.status_code == 200:
           data = data.json()
           #data = json.loads(data)
           #data = namedtuple("data",data)





        else:
            data = {'Error': 'There was a problem with your provided ticker symbol. Please try again'}

    return render(request, 'index.html', context={'data': data})


def signin(request):
    if request.method == 'GET':
        form1 = AuthenticationForm()
        context = {
            "form": form1
        }
        return render(request, 'signin.html', context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request, user)
                return redirect('/')
        else:
            context = {
                "form": form
            }
            return render(request, 'signin.html', context=context)


def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form": form
        }
        return render(request, 'signup.html', context=context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        context = {
            "form": form
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('signin')
        else:
            return render(request, 'signup.html', context=context)


def signout(request):
    logout(request)
    return redirect('signin')



