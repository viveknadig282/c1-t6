from django.urls import path
from . import views #importing views file

urlpatterns = [
    path('results/', views.resultspage, name='results'), #mapping the resultspage function
    path("", views.homepage, name="home"), #mapping the homepage function
]