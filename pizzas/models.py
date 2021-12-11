from django.db import models


class Pizza(models.Model):
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()


    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        return self.name