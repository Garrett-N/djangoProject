from django.shortcuts import render


# Create your views here.
def projectview(request):
    return render(request, 'project.html')