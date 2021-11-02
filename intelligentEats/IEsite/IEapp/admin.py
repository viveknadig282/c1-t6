from django.contrib import admin

# Register your models here.

from .models import scraper_articles, ingredients, food, ingredient_food

admin.site.register(scraper_articles)

admin.site.register(ingredients)

admin.site.register(food)

admin.site.register(ingredient_food)