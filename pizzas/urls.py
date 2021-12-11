from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('pizza_menu/', views.pizza_menu, name='pizza_menu'),
    path('pizza_menu/<int:pizza_id>', views.pizza_ingredients, name='pizza_ingredients'),
]