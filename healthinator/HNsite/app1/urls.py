from django.urls import path

from . import views #importing views file

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.homepage, name='home'), #mapping the homepage function
]