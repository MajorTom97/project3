from django.http import HttpResponse
from django.shortcuts import redirect, render
from orders.forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

login_required(login_url='signin')
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
                login(request, username)
                return redirect('index')
            else:
                messages.info(request, 'Username or Password is incorrect!')
        context = {}
        return render (request, "signin.html", context)

def signoutUser(request):
    logout(request)
    return 

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:

        form = UserCreationForm()
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                messages.success(request, f'User {username} successfully registered')
                return redirect('register')
        else:
            form = UserCreationForm()
    
    context = {'form': form}
    return render(request, "register.html", context)   