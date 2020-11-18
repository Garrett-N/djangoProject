from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def Home(request):
    context = {
        "name":"Garrett N",
        "lucky_number":59,
        "list_friends":["steve", "gary", "pam", "sue"]

    }
    return render(request, 'home.html', context)

def K9gbn(request):
    return HttpResponse("<h1>k9gbn app</h1>")