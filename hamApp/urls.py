from django.urls import path
from .views import homeview, hamview

urlpatterns = [
    path('', homeview),
    path('k9gbn/', hamview),
]
