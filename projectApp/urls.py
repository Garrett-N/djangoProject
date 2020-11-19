from django.urls import path
from .views import projectview

urlpatterns = [
    path('', projectview),
]