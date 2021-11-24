from django.contrib import admin
from .models import Category, Extras, Pastas, RegularPizza, Salads, SicilianPizza, Subs, Toppings, DinnerPlatters

# Register your models here.

admin.site.register(Category)
admin.site.register(Toppings)
admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)
admin.site.register(Extras)
admin.site.register(Subs)
admin.site.register(Pastas)
admin.site.register(Salads)
admin.site.register(DinnerPlatters)