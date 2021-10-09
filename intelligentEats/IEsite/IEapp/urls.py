from django.urls import path
from . import views #importing views file

urlpatterns = [
    path("", views.homepage, name="home"), #mapping the homepage function
]