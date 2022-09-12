"""Defines URl patterns for Pizzas."""

from django.urls import path

from . import views

app_name = 'pizzas'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows available pizzas.
    path('pizzas/', views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza')
]

