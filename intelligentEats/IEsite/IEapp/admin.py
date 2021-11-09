from django.contrib import admin

# Register your models here.

from .models import ScraperArticle, Ingredient, Food, IngredientFood

admin.site.register(ScraperArticle)

admin.site.register(Ingredient)

admin.site.register(Food)

admin.site.register(IngredientFood)