from django.shortcuts import render #for rendering templates

# Create your views here.

def homepage(request):
    return render(request, 'index.html', context={})

def resultspage(request):
    return render(request, 'results.html', context={})