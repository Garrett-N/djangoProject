from django.shortcuts import render


# Create your views here.
def homeview(request):
    context = {
        "name":"Garrett N",
        "lucky_number":59,
        "list_friends":["steve", "gary", "pam", "sue"]
    }
    return render(request, 'home.html', context)


def hamview(request):
    return render(request, 'k9gbn.html')
