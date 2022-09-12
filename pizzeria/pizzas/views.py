from django.shortcuts import render

from .models import Pizza


def index(request):
    """The home page for Pizzeria."""
    return render(request, 'pizzas/index.html')


def pizzas(request):
    """Show all pizzas."""
    pizzas = Pizza.objects.order_by('topping')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)


def pizza(request, pizza_id):
    """Show a single pizza and all the toppings"""
    pizza = Pizza.object.get(id=pizza_id)
    topping = pizza.topping_set.order_by('topping')
    context = {'pizza': pizza, 'topping': topping}
    return render(request, 'pizzas/pizza.html', context)














