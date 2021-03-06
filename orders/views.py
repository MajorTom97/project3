from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from orders.models import Order, OrderDetail, RegularPizza, SicilianPizza, Toppings, Subs, Pastas, Salads, Extras, Category, DinnerPlatters
from .forms import  UserRegisterForm

# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            return redirect('index')
        else:
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'User {username} successfully registered')
                return redirect('login')
            else:
                print(form.errors)
                return redirect('register')
    
    form = UserRegisterForm()
    context = {'form': form}
    return render(request, "register.html", context)  

# Categories 

def Menu(request):
    if request.method == 'GET':
        
        reg_pizza = RegularPizza.objects.all()
        sici_pizza = SicilianPizza.objects.all()
        toppings = Toppings.objects.all()

        subs = Subs.objects.all()
        extras = Extras.objects.all()

        pasta = Pastas.objects.all()

        salads = Salads.objects.all()

        platters = DinnerPlatters.objects.all()

        context = {
            "reg_pizzas":reg_pizza, #
            "sici_pizzas": sici_pizza, #
            "toppings": toppings,
            "subs": subs, #
            "extras": extras,
            "pastas":pasta,
            "salads":salads,
            "platters":platters, #

        }

        return render(request,"menu.html", context)
    else:
        product = request.POST.get("product")
        quantity = int(request.POST.get("quantity"))
        price = float(request.POST.get("price"))
        toppings = request.POST.getlist("toppings")
        order = OrderPending(request.user)
        toppingObject=[]

        for topping in toppings:
            toppingObject.append(Toppings.objects.get(pk=topping))
        detailOr = OrderDetail.objects.create(order=order, product=product, price=price, quantity=quantity, subtotal=(float(quantity)*price))
        if toppings:
            for topping in toppingObject:
                detailOr.toppings.add(topping)
        
        order.total = float(order.total) + float(detailOr.subtotal)
        order.save()

        print(request.POST)
        return redirect("menu")

def OrderPending(user):
    order = Order.objects.filter(user=user, pending=True).first()
    if not order:
        order = Order.objects.create(user=user, total=0)
    return order

def cart(request):
    return render(request,"cart.html", {"orders": [OrderPending(request.user), ]})

def history(request):
    return render(request,"cart.html", {"orders": Order.objects.filter(user = request.user).all()})

def buy(request):
    order = OrderPending(request.user)
    order.pending = False
    order.save()
    return redirect("menu")