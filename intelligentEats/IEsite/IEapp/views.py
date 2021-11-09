from django.shortcuts import render #for rendering templates
from .models import Food, Ingredient, IngredientFood, ScraperArticle
from IEapp.FoodAPI import FoodAPI
from django.http import JsonResponse

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

def upc(request, upc_code):
    api = FoodAPI(None, None)
    query_result = get_data(api.get_ingredients(upc_code))
    return JsonResponse(list(query_result), safe=False)

def ingredient_scores(request, ingredient_list):
    query_result = get_data(ingredient_list.split(','))
    return JsonResponse(list(query_result), safe=False)

def get_data(ingredient_array):
    return Ingredient.objects.filter(name__in=ingredient_array).values('name', 'score')
