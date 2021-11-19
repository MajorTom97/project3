from django.db import models

# Create your models here.

class Category(models.Model):
    categories = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return f"Category Added {self.categories}"

class Pizzas(models.Model):
    pizza = models.CharField(max_length=20)

    def __str__(self):
        return f"You have choosed{self.pizza}"

class Toppings(models.Model):
    topping = models.CharField(max_length=20)

    def __str__(self):
        return f"Added {self.topping}"

class DinnerPlatters(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey