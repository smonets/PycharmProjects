from django.shortcuts import render
from .models import Pizza


def index(request):
    return render(request, 'pizzas/index.html')


def pizza_menu(request):
    pizzas = Pizza.objects.order_by('date_added')
    context = {"pizzas": pizzas}
    return render(request, 'pizzas/pizza_menu.html', context)


def pizza_ingredients(request, pizza_id):
    pizza_name = Pizza.objects.get(id=pizza_id)
    toppings = pizza_name.topping_set.all()
    context = {'toppings': toppings,
              'pizza_name': pizza_name }
    return render(request, 'pizzas/ingredients.html', context)