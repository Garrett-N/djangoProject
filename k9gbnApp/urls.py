from django.urls import path
from .views import K9gbn, Home

urlpatterns = [
    path('', Home, name='home'),
    path('k9gbn/', K9gbn, name = 'k9gbn'),
]
