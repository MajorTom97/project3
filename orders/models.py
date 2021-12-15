from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Category(models.Model):
    categories = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return f"Category Added {self.categories}"
    
    class Meta:
        verbose_name_plural="Categories"

class Toppings(models.Model):
    topping = models.CharField(max_length=20)

    def __str__(self):
        return f"Added {self.topping}"
    
    class Meta:
        verbose_name_plural="Toppings"

class RegularPizza(models.Model):
    pizza = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="regularPrice")
    small = models.DecimalField(max_digits=5, decimal_places=2)
    large = models.DecimalField(max_digits=5, decimal_places=2)
    max_toppings = models.IntegerField(default=0)

    def __str__(self):
        return f"Regular {self.pizza} - Small:{self.small} Large:{self.large}"

    class Meta:
        verbose_name_plural="RegularPizza"
class SicilianPizza(models.Model):
    pizza = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="sicilianPrice")
    small = models.DecimalField(max_digits=5, decimal_places=2)
    large = models.DecimalField(max_digits=5, decimal_places=2)
    max_toppings = models.IntegerField(default=0)

    def __str__(self):
        return f"Sicilian {self.pizza} - Small:{self.small} Large:{self.large}"

    class Meta:
        verbose_name_plural="SicilianPizza"

class Extras(models.Model):
    addition = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.addition}"

    class Meta:
        verbose_name_plural="Extras"
class Pastas(models.Model):
    pasta = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.pasta} - Price:{self.price}"

    class Meta:
        verbose_name_plural="Pastas"
class Salads(models.Model):
    salad = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.salad} - Price:{self.price}"
    class Meta:
        verbose_name_plural="Salads"
class DinnerPlatters(models.Model):
    dinner = models.CharField(max_length=20)
    small = models.DecimalField(max_digits=5, decimal_places=2)
    large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.dinner} - Small:{self.small} - Large:{self.large}"

    class Meta:
        verbose_name_plural="DinnerPlatters"
class Subs(models.Model):
    sub = models.CharField(max_length=30)
    small = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    large = models.DecimalField(max_digits=5, decimal_places=2)
    max_toppings = models.IntegerField(default=3)
    
    def __str__(self):
        return f"Sub {self.sub} - Small:{self.small} - Large:{self.large}"
    class Meta:
        verbose_name_plural="Subs"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="orders")
    total = models.FloatField()
    pending = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True)
    
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=CASCADE, related_name="details")
    product = models.CharField(max_length = 200)
    quantity = models.IntegerField()
    price = models.FloatField()
    subtotal = models.FloatField()
    toppings = models.ManyToManyField(Toppings)