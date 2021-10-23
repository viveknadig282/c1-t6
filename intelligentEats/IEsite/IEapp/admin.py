from django.contrib import admin

from .models import scraper_articles
from .models import ingredients
from .models import food
from .models import ingredient_food

admin.site.register(food)
# Register your models here.
