from django.contrib import admin
from .models import Pizza


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('pizza_name', 'ingredients', 'vegetarian', 'price')
    search_fields = ['pizza_name']



admin.site.register(Pizza, PizzaAdmin)