from django.db import models


class Pizza(models.Model):
    """A name of a pizza."""
    name = models.CharField(max_length=50)

    def __str__(self):
        """Returns string representation of the model."""
        return self.name


class Topping(models.Model):
    """The type of topping on the pizza"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    pizza_topping = models.CharField(max_length=50)

    def __str__(self):
        """Returns string representation of the model."""
        return self.pizza_topping
