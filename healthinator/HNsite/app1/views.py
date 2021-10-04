from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

#def index(request):
    #return HttpResponse("Your food is mad healthy bro.")

def homepage(request):
    return render(request, 'index.html', context={})