from django.contrib import admin
from .models import Category, Pizzas, Toppings, DinnerPlatters

# Register your models here.

admin.site.register(Category)
admin.site.register(Pizzas)
admin.site.register(Toppings)
admin.site.register(DinnerPlatters)