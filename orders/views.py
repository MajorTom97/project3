from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from orders.models import RegularPizza, SicilianPizza, Toppings, Subs, Pastas, Salads, Extras, Category, DinnerPlatters
from .forms import CreateUserForm

# Create your views here.

@login_required(login_url='signin')
def index(request):
    return render(request, "index.html")

def singin(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or Password is incorrect!')
        context = {}
        return render (request, "signin.html", context)

def signoutUser(request):
    logout(request)
    messages.success(request, 'Come back soon!')
    return HttpResponse

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'User {username} successfully registered')
                return redirect('signin')


        context = {'form': form}
        return render(request, "register.html", context)  

def Category(request):
    reg_pizza = RegularPizza.objects.all()
    sici_pizza = SicilianPizza.objects.all()
    toppings = Toppings.objects.all()

    context = {
        "reg_pizzas":reg_pizza,
        "sici_pizza": sici_pizza,
        "toppinngs": toppings
    }

    return render(request,"menu.html", context)

def subs(request):
    subs = Subs.objects.all()
    extras = Extras.objects.all()
    context = {
        "subs": subs,
        "extras": extras
    }

    return render(request, "menu.html", context)

def pasta(request):
    pasta = Pastas.objects.all()
    return render(request, "menu.html", {"pasta":pasta})

def salads(request):
    salads = Salads.objects.all()
    return render (request, "menu.html", {"salads":salads})

def dinnerPlatters(request):
    platters = DinnerPlatters.objects.all()
    context = {
        "platters":platters
    }
    return render(request, "menu.html", context)
