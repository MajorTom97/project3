from django.http import HttpResponse
from django.shortcuts import render
from orders.forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    return render(request, "index.html")

def singin(request):
    return render (request, "signin.html")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, "register.html", context)   