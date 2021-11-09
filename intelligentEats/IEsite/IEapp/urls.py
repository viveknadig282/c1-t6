from django.urls import path
from . import views #importing views file

urlpatterns = [
    path('ingredients/<str:ingredient_list>', views.ingredient_scores, name='ingredients'), #mapping the ingredient function
    path('upc/<str:upc_code>', views.upc, name='upc'), #mapping the upc function
    path('results/', views.resultspage, name='results'), #mapping the resultspage function
    path("", views.homepage, name="home"), #mapping the homepage function

    path('food/', views.foodpage, name='list-food'),
    path('ingredient/', views.ingredientpage, name='list-ingredient'),
]
