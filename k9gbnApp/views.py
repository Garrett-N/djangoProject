from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def Home(request):
    #return HttpResponse("<h1>This is the main page</h1>")
    return render(request, 'home.html')

def K9gbn(request):
    return HttpResponse("<h1>k9gbn app</h1>")