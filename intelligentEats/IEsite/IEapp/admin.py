from django.contrib import admin

# Register your models here.

from .models import ScraperArticles, Ingredients, Food, IngredientFood

admin.site.register(ScraperArticles)

admin.site.register(Ingredients)

admin.site.register(Food)

admin.site.register(IngredientFood)