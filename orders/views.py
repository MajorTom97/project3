from django.http import HttpResponse
from django.shortcuts import render

from orders.forms import UserRegisterForm

# Create your views here.
def index(request):
    return render(request, "index.html")

def singin(request):
    return render (request, "signin.html")

def register(request):
    if request.method == "POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            newUser=form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']