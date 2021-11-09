from django.shortcuts import render #for rendering templates
from .models import Food, Ingredient, IngredientFood, ScraperArticle
# Create your views here.

def homepage(request):
    return render(request, 'index.html', context={})

def resultspage(request):
    return render(request, 'results.html', context={})

def foodpage(request):
    food_list = Food.objects.all()
    
    return render(request, 'food_list.html', context={'food_list': food_list})
def ingredientpage(request):
    ingredient_list = Ingredient.objects.all()
    return render(request, 'ingredient_list.html', context={'ingredient_list':ingredient_list})